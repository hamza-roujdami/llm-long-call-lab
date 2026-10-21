"""Traces and metrics to Application Insights (the one connected to the Foundry project).

MAF emits OpenTelemetry gen-ai spans (agent runs, chat calls, tool calls, workflow steps); Azure Monitor
exports them. Our HTTP-level timings are added to the active span (see annotate_span) so the Foundry
Traces view shows time to headers, first token and longest silent gap next to each model call.
Prompt/response content is NOT recorded (it would be ~100K tokens per span).
"""

import logging
import os
from typing import Any

log = logging.getLogger("tracing")
_enabled = False


def setup_tracing(service_name: str) -> bool:
    """Enable export when APPLICATIONINSIGHTS_CONNECTION_STRING is set. Safe to call twice."""
    global _enabled
    conn = os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING", "")
    if _enabled or not conn:
        return _enabled
    try:
        from agent_framework.observability import enable_instrumentation
        from azure.monitor.opentelemetry import configure_azure_monitor

        os.environ.setdefault("OTEL_SERVICE_NAME", service_name)
        # The distro's default sampler keeps ~5 traces/s and drops spans from bursty agent runs: keep all.
        configure_azure_monitor(connection_string=conn, sampling_ratio=1.0)
        enable_instrumentation(enable_sensitive_data=False)
        _log_ended_spans()
        _enabled = True
    except Exception as e:  # noqa: BLE001 - telemetry must never break a run
        log.warning("tracing disabled: %s: %s", type(e).__name__, e)
    return _enabled


def _log_ended_spans() -> None:
    """Print one `SPAN name duration` console line per ended span: a second record next to the export."""
    from opentelemetry import trace
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor, SpanExporter, SpanExportResult

    class _Console(SpanExporter):
        def export(self, spans):
            for sp in spans:
                ms = (sp.end_time - sp.start_time) / 1e6
                print(
                    f"SPAN {sp.name} {ms:.0f}ms trace={sp.context.trace_id:032x}"[:200], flush=True
                )
            return SpanExportResult.SUCCESS

    provider = trace.get_tracer_provider()
    if hasattr(provider, "add_span_processor"):
        provider.add_span_processor(SimpleSpanProcessor(_Console()))


def flush_tracing() -> None:
    """Export everything before a short-lived job exits."""
    if not _enabled:
        return
    try:
        from opentelemetry import metrics, trace

        for provider in (trace.get_tracer_provider(), metrics.get_meter_provider()):
            flush = getattr(provider, "force_flush", None)
            if flush:
                flush()
    except Exception:  # noqa: BLE001
        pass


def annotate_span(rec: dict[str, Any]) -> None:
    """Put the measured timings of one HTTP call on the current span (best effort)."""
    try:
        from opentelemetry import trace

        span = trace.get_current_span()
        if not span.is_recording():
            return
        for key in (
            "path", "stream", "http_status", "outcome", "ttfh_s", "ttfb_s", "ttft_s",
            "longest_gap_s", "tail_silence_s", "total_s", "request_ids",
        ):  # fmt: skip
            if rec.get(key) is not None:
                span.set_attribute(f"lab.{key}", rec[key])
    except Exception:  # noqa: BLE001
        pass


def run_span(name: str, **attrs: Any):
    """Context manager: a parent span for a whole run (no-op if tracing is off)."""
    from contextlib import nullcontext

    if not _enabled:
        return nullcontext()
    from opentelemetry import trace

    tracer = trace.get_tracer("apim-timeout-lab")
    return tracer.start_as_current_span(name, attributes={f"lab.{k}": v for k, v in attrs.items()})

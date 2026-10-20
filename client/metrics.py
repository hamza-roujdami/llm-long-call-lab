"""Pure measurement helpers and the CSV schema (no network, easily unit-tested)."""

from dataclasses import asdict, dataclass, field, fields

DONE_MARKERS = (b"[DONE]", b'"done":true', b'"done": true')


@dataclass
class Result:
    run_id: str = ""
    started_utc: str = ""
    scenario: str = ""
    hypothesis: str = ""
    target: str = ""  # direct | apim
    path: str = ""  # request path (without query)
    query: str = ""
    client_stream: bool = False
    parallel_index: int = 0
    parallel_total: int = 1
    http_status: int | None = None
    outcome: str = ""  # completed | truncated | http_error | error
    error_type: str = ""
    error_detail: str = ""
    ttfh_s: float | None = None  # time to response headers
    ttfb_s: float | None = None  # time to first body byte (stream mode only)
    longest_gap_s: float | None = None  # longest gap between body chunks (stream mode only)
    last_chunk_s: float | None = None  # time of last chunk (stream mode only)
    chunks: int = 0
    bytes: int = 0
    total_s: float | None = None
    client_request_id: str = ""
    server_request_ids: str = ""  # header=value pairs seen on the response
    extra: dict[str, str] = field(default_factory=dict)

    def row(self) -> dict[str, object]:
        d = asdict(self)
        d["extra"] = ";".join(f"{k}={v}" for k, v in self.extra.items())
        return d


CSV_COLUMNS = [f.name for f in fields(Result)]

# Response headers that can correlate a call with APIM gateway logs or the mock's logs.
ID_HEADERS = (
    "x-ms-request-id",
    "request-id",
    "x-request-id",
    "apim-request-id",
    "x-ms-client-request-id",
    "x-mock-request-id",
)


def longest_gap(times: list[float]) -> float | None:
    """Longest interval between consecutive chunk arrival times (seconds, ascending)."""
    if len(times) < 2:
        return None
    return max(b - a for a, b in zip(times, times[1:], strict=False))


def has_done_marker(tail: bytes) -> bool:
    return any(m in tail for m in DONE_MARKERS)


def classify(status: int | None, saw_done: bool, error: BaseException | None) -> str:
    if status is None:
        return "error"
    if not 200 <= status < 300:
        return "http_error"
    if error is not None or not saw_done:
        return "truncated"
    return "completed"


def pick_ids(headers: dict[str, str]) -> str:
    lowered = {k.lower(): v for k, v in headers.items()}
    return ";".join(f"{h}={lowered[h]}" for h in ID_HEADERS if h in lowered)

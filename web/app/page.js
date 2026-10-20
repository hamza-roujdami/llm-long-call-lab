"use client";

import { useCallback, useEffect, useState } from "react";

const card = { background: "#fff", border: "1px solid #dde1e6", borderRadius: 8, padding: 16, marginBottom: 16 };
const th = { textAlign: "left", padding: "4px 8px", borderBottom: "1px solid #dde1e6", whiteSpace: "nowrap" };
const td = { padding: "4px 8px", borderBottom: "1px solid #eef0f2", whiteSpace: "nowrap" };
const badge = (s) => ({
  padding: "2px 8px",
  borderRadius: 10,
  fontSize: 12,
  background: { succeeded: "#d6f5dd", failed: "#fbd9d9", running: "#fff1c2", queued: "#e6e9ee" }[s] || "#e6e9ee",
});
const fmt = (v) => (v === undefined || v === null || v === "" ? "" : typeof v === "number" ? Number(v.toFixed(2)) : v);

export default function Home() {
  const [form, setForm] = useState({
    path: "direct", gateway_variant: "stream", stream: true, api: "responses", reasoning_effort: "high",
    fact_tokens: 80000, max_output_tokens: 16000, depth: "normal", rounds: 1, note: "",
  });
  const [runs, setRuns] = useState([]);
  const [sel, setSel] = useState(null);
  const [run, setRun] = useState(null);
  const [error, setError] = useState("");

  const loadRuns = useCallback(async () => {
    const r = await fetch("/api/runs");
    if (r.ok) setRuns(await r.json());
  }, []);

  useEffect(() => {
    loadRuns();
    const t = setInterval(loadRuns, 5000);
    return () => clearInterval(t);
  }, [loadRuns]);

  useEffect(() => {
    if (!sel) return;
    let stop = false;
    const tick = async () => {
      const r = await fetch(`/api/runs/${sel}`);
      if (!r.ok || stop) return;
      const data = await r.json();
      setRun(data);
      if (data.status === "queued" || data.status === "running") setTimeout(tick, 3000);
    };
    tick();
    return () => { stop = true; };
  }, [sel]);

  async function start(e) {
    e.preventDefault();
    setError("");
    const r = await fetch("/api/runs", {
      method: "POST",
      body: JSON.stringify({ ...form, fact_tokens: Number(form.fact_tokens), max_output_tokens: Number(form.max_output_tokens), rounds: Number(form.rounds) }),
    });
    if (!r.ok) return setError(`${r.status}: ${(await r.text()).slice(0, 300)}`);
    const { run_id } = await r.json();
    setRun(null);
    setSel(run_id);
    loadRuns();
  }

  const set = (k) => (e) => setForm({ ...form, [k]: e.target.type === "checkbox" ? e.target.checked : e.target.value });
  const summary = run?.summary_json ? JSON.parse(run.summary_json) : run?.live_summary;

  return (
    <main style={{ maxWidth: 1180, margin: "0 auto", padding: 24 }}>
      <h1 style={{ marginTop: 0 }}>APIM timeout lab</h1>
      <p style={{ color: "#555" }}>
        Start a synthetic HLD→LLD run (planner + 4 section agents, GPT-6 Sol) over a chosen path and watch per-call timing.
      </p>

      <form onSubmit={start} style={{ ...card, display: "flex", flexWrap: "wrap", gap: 16, alignItems: "end" }}>
        <label>Path<br />
          <select value={form.path} onChange={set("path")}>
            <option value="direct">Direct to Foundry</option>
            <option value="gateway">Via APIM</option>
          </select>
        </label>
        {form.path === "gateway" && (
          <label>APIM config<br />
            <select value={form.gateway_variant} onChange={set("gateway_variant")}>
              <option value="default">A: default policy (buffered)</option>
              <option value="stream">B: buffer-response=false, timeout 600</option>
            </select>
          </label>
        )}
        <label><input type="checkbox" checked={form.stream} onChange={set("stream")} /> Stream</label>
        <label>API<br />
          <select value={form.api} onChange={set("api")}>
            <option value="responses">Responses</option>
            <option value="chat">Chat Completions</option>
          </select>
        </label>
        <label>Reasoning<br />
          <select value={form.reasoning_effort} onChange={set("reasoning_effort")}>
            {["none", "minimal", "low", "medium", "high"].map((x) => <option key={x}>{x}</option>)}
          </select>
        </label>
        <label>Depth<br />
          <select value={form.depth} onChange={set("depth")}>
            <option value="normal">normal (~1.5 min planner)</option>
            <option value="exhaustive">exhaustive (planner checks every fact, minutes)</option>
          </select>
        </label>
        <label>Max output (tokens)<br />
          <input type="number" min="256" max="128000" step="1000" value={form.max_output_tokens} onChange={set("max_output_tokens")} style={{ width: 100 }} />
        </label>
        <label>Planner facts (est. tokens, ×1.25 real)<br />
          <input type="number" min="1000" max="400000" step="1000" value={form.fact_tokens} onChange={set("fact_tokens")} style={{ width: 110 }} />
        </label>
        <label>Rounds<br />
          <input type="number" min="1" max="20" value={form.rounds} onChange={set("rounds")} style={{ width: 60 }} />
        </label>
        <label>Note<br /><input value={form.note} onChange={set("note")} maxLength={200} /></label>
        <button type="submit" style={{ padding: "8px 18px", fontWeight: 600 }}>Start run</button>
        {error && <span style={{ color: "#b00020" }}>{error}</span>}
      </form>

      <div style={{ display: "grid", gridTemplateColumns: "300px 1fr", gap: 16 }}>
        <section style={card}>
          <h3 style={{ marginTop: 0 }}>Runs</h3>
          {runs.length === 0 && <em>none yet</em>}
          {runs.map((r) => (
            <div key={r.id} onClick={() => setSel(r.id)}
              style={{ cursor: "pointer", padding: "6px 0", fontWeight: r.id === sel ? 700 : 400 }}>
              <span style={badge(r.status)}>{r.status}</span> {r.id}
              <div style={{ fontSize: 12, color: "#666" }}>{r.note}</div>
            </div>
          ))}
        </section>

        <section style={card}>
          {!run && <em>Select or start a run.</em>}
          {run && (
            <>
              <h3 style={{ marginTop: 0 }}>
                {run.id} <span style={badge(run.status)}>{run.status}</span>
              </h3>
              <div style={{ fontSize: 14, color: "#444" }}>
                {run.phase} · progress {run.progress || "0"} · config <code>{run.config_json}</code>
              </div>
              {run.error && <p style={{ color: "#b00020" }}>{run.error}</p>}
              {summary && (
                <p style={{ fontSize: 14 }}>
                  calls {summary.llm_calls} (failed {summary.failed_calls}) · max first-byte {fmt(summary.max_ttfb_s)}s ·
                  longest gap {fmt(summary.max_longest_gap_s)}s · longest call {fmt(summary.max_call_total_s)}s ·
                  tokens in/out/reasoning {summary.prompt_tokens}/{summary.completion_tokens}/{summary.reasoning_tokens}
                  {summary.elapsed_s !== undefined && <> · elapsed {summary.elapsed_s}s</>}
                </p>
              )}
              <p>
                <a href={`/api/runs/${run.id}/calls.csv`}>calls.csv</a> ·{" "}
                <a href={`/api/runs/${run.id}/output`} target="_blank">output.json</a>
              </p>
              <div style={{ overflowX: "auto" }}>
                <table style={{ borderCollapse: "collapse", fontSize: 13 }}>
                  <thead>
                    <tr>{["rnd", "agent", "kind", "turn", "att", "http", "outcome", "ttfh s", "ttfb s", "longest gap s", "total s", "in", "out", "reasoning", "error"].map((h) => <th key={h} style={th}>{h}</th>)}</tr>
                  </thead>
                  <tbody>
                    {(run.calls || []).map((c, i) => (
                      <tr key={i}>
                        {[c.round, c.agent, c.kind === "tool" ? c.path : "llm", c.turn, c.attempt, c.http_status, c.outcome, c.ttfh_s, c.ttfb_s, c.longest_gap_s, c.total_s, c.prompt_tokens, c.completion_tokens, c.reasoning_tokens, c.error_type].map((v, j) => (
                          <td key={j} style={{ ...td, color: j === 6 && v && v !== "completed" ? "#b00020" : undefined }}>{fmt(v)}</td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          )}
        </section>
      </div>
    </main>
  );
}

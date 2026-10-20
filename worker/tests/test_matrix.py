import asyncio

import pytest

from worker import run_matrix
from worker.llm_client import CallResult
from worker.tests import fake_model


def run(coro):
    return asyncio.run(coro)


def fake_call(duration_for, cap=10**9, outcome="completed", tokens=100):
    async def call(n: int) -> CallResult:
        rec = {
            "total_s": duration_for(n),
            "ttft_s": 2.0,
            "outcome": outcome,
            "completion_tokens": tokens,
            "http_status": 200,
        }
        return CallResult("x", rec, "" if outcome == "completed" else "boom")

    return call


def test_calibration_converges_on_a_linear_model():
    res = run(
        run_matrix.calibrate(
            "S", 300, fake_call(lambda n: 2 + 0.25 * n), n_max=5000, cap=10**9, start=250
        )
    )
    assert res["status"] == "ok" and abs(res["measured_s"] - 300) <= 45
    assert len(res["history"]) >= 2  # a small probe first, then the scaled call


def test_calibration_stops_when_facts_run_out():
    res = run(run_matrix.calibrate("L", 450, fake_call(lambda n: 0.01 * n), n_max=1000, cap=10**9))
    assert res["status"] == "failed" and "needs more than 1000 facts" in res["reason"]


def test_calibration_stops_when_the_cap_truncates_the_answer():
    call = fake_call(lambda n: 100.0, tokens=990)
    res = run(run_matrix.calibrate("S", 300, call, n_max=5000, cap=1000))
    assert res["status"] == "failed" and "cap" in res["reason"]


def test_calibration_stops_on_a_failed_call():
    res = run(
        run_matrix.calibrate(
            "S", 300, fake_call(lambda n: 5.0, outcome="truncated"), n_max=99, cap=9
        )
    )
    assert res["status"] == "failed"


def test_plan_is_the_full_matrix():
    cells = run_matrix.plan_cells(
        ["S", "L"], ["direct", "apim-default", "apim-stream"], [False, True], 1
    )
    assert len(cells) == 12 and len(set(cells)) == 12
    assert len(run_matrix.plan_cells(["S"], ["direct"], [True], 3)) == 3


def test_cost_guard_dry_run_never_calls_the_model(capsys, monkeypatch):
    def boom(*a, **k):
        raise AssertionError("model must not be constructed on a dry run")

    monkeypatch.setattr(run_matrix, "Model", boom)
    code = run(run_matrix.amain(run_matrix.parse_args(["--max-output-tokens", "1000"])))
    out = capsys.readouterr().out
    assert code == 0 and "DRY RUN" in out and "worst case" in out


def test_max_output_tokens_is_required():
    with pytest.raises(SystemExit):
        run_matrix.parse_args([])


def test_matrix_cells_run_and_write_csv(live_fake, monkeypatch, tmp_path):
    monkeypatch.setenv("LLM_BASE_URL_OVERRIDE", live_fake)
    monkeypatch.setenv("RESULTS_DIR", str(tmp_path))
    monkeypatch.setattr(run_matrix, "load_calibration", lambda: {"S": {"n_facts": 3}})
    args = run_matrix.parse_args(
        ["--max-output-tokens", "100", "--confirm-spend", "--skip-calibration", "--prompts", "S"]
    )
    assert run(run_matrix.amain(args)) == 0
    rows = (tmp_path / "runs.csv").read_text().splitlines()
    assert len(rows) == 1 + 6  # 3 paths x stream off/on
    assert fake_model.FIRST_DELAY == 0.0
    assert sum("direct|stream=on|S|r1" in r for r in rows) == 1
    assert all(",completed," in r for r in rows[1:])


def test_matrix_args_work_without_dashes():
    from worker.__main__ import matrix_argv

    assert matrix_argv(["max-output-tokens=1000", "confirm-spend", "--repeat=2"]) == [
        "--max-output-tokens", "1000", "--confirm-spend", "--repeat", "2",
    ]  # fmt: skip

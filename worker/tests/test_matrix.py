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
        [
            "--max-output-tokens",
            "100",
            "--confirm-spend",
            "--skip-calibration",
            "--prompts",
            "S",
            "--cooldown-s",
            "0",
        ]
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


def test_cooldown_spaces_consecutive_calls(live_fake, monkeypatch, tmp_path):
    monkeypatch.setenv("LLM_BASE_URL_OVERRIDE", live_fake)
    monkeypatch.setenv("RESULTS_DIR", str(tmp_path))
    monkeypatch.setattr(run_matrix, "load_calibration", lambda: {"S": {"n_facts": 2}})
    args = run_matrix.parse_args(
        ["--max-output-tokens", "100", "--confirm-spend", "--skip-calibration", "--prompts", "S",
         "--paths", "direct", "--streams", "off", "--repeat", "2", "--cooldown-s", "1.5"]
    )  # fmt: skip
    import time

    t0 = time.monotonic()
    assert run(run_matrix.amain(args)) == 0
    assert time.monotonic() - t0 >= 1.4  # the second cell waited for the cooldown


def test_calibration_steps_are_clamped_and_converge():
    sizes = []

    async def call(n: int) -> CallResult:
        sizes.append(n)
        return await fake_call(lambda m: 2 + 0.25 * m)(n)

    res = run(run_matrix.calibrate("S", 300, call, n_max=5000, cap=10**9, start=100))
    assert res["status"] == "ok"
    assert all(
        b <= 2 * a for a, b in zip(sizes, sizes[1:], strict=False)
    )  # never more than 2x per step


def test_fit_items_respects_the_input_token_budget():
    items = [{"id": f"c{i}.0", "text": "x" * 100} for i in range(1000)]
    n = run_matrix.fit_items(items, 5000)
    assert 0 < n < 1000 and run_matrix.fit_items(items, 10**9) == 1000


def test_known_calibration_is_reused_without_calling_the_model(live_fake, monkeypatch, tmp_path):
    monkeypatch.setenv("LLM_BASE_URL_OVERRIDE", live_fake)
    monkeypatch.setenv("RESULTS_DIR", str(tmp_path))
    args = run_matrix.parse_args(
        ["--max-output-tokens", "100", "--confirm-spend", "--known", "S=3", "--prompts", "S",
         "--paths", "direct", "--streams", "off", "--cooldown-s", "0"]
    )  # fmt: skip
    assert run(run_matrix.amain(args)) == 0
    rows = (tmp_path / "runs.csv").read_text().splitlines()
    assert len(rows) == 2 and "calibrate" not in rows[1] and "direct|stream=off|S|r1" in rows[1]


def test_L_keeps_the_items_and_calibrates_the_words(live_fake, monkeypatch, tmp_path):
    from worker.prompts import build_prompt, system_prompt

    assert "40 to 50 words" in system_prompt(45) and "25 to 35 words" in system_prompt()
    system, user = build_prompt(3, [{"id": "a", "text": "t"}] * 5, 60)
    assert "55 to 65 words" in system and '"fact_count": 3' in user

    monkeypatch.setenv("LLM_BASE_URL_OVERRIDE", live_fake)
    monkeypatch.setenv("RESULTS_DIR", str(tmp_path))
    args = run_matrix.parse_args(
        ["--max-output-tokens", "100", "--confirm-spend", "--known", "S=4,L=60", "--prompts", "S,L",
         "--paths", "direct", "--streams", "off", "--cooldown-s", "0"]
    )  # fmt: skip
    assert run(run_matrix.amain(args)) == 0
    assert (
        len((tmp_path / "runs.csv").read_text().splitlines()) == 1 + 2
    )  # S and L cells, no calibration


def test_verdict_flags_calls_too_short_to_test_the_limits():
    assert "TOO SHORT" in run_matrix.verdict({"outcome": "completed", "total_s": 100})
    assert "TOO SHORT" not in run_matrix.verdict({"outcome": "completed", "total_s": 300})
    cut = run_matrix.verdict(
        {"outcome": "truncated", "http_status": 200, "error_type": "X", "total_s": 100}
    )
    assert "truncated" in cut and "TOO SHORT" not in cut  # a cut is data at any duration

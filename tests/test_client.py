import csv
import json

from client.logs_to_csv import parse_lines
from client.metrics import CSV_COLUMNS, Result, classify, has_done_marker, longest_gap, pick_ids
from client.run import Settings, build_request, write_csv
from client.scenarios import SCENARIOS


def test_longest_gap():
    assert longest_gap([]) is None
    assert longest_gap([1.0]) is None
    assert longest_gap([0.0, 1.0, 301.0, 302.0]) == 300.0


def test_classify():
    assert classify(None, False, OSError()) == "error"
    assert classify(504, False, None) == "http_error"
    assert classify(200, False, None) == "truncated"
    assert classify(200, True, OSError()) == "truncated"
    assert classify(200, True, None) == "completed"


def test_done_markers():
    assert has_done_marker(b"data: [DONE]\n\n")
    assert has_done_marker(b'{"done":true}')
    assert not has_done_marker(b'data: {"seq": 1}\n\n')


def test_pick_ids_case_insensitive():
    assert pick_ids({"X-MS-Request-Id": "abc", "other": "x"}) == "x-ms-request-id=abc"


def test_matrix_scenarios_present():
    for name in [
        "direct-silent-300",
        "direct-silent-450",
        "apim-silent-300",
        "apim-stream-450",
        "apim-gap-300",
        "apim-stream-buffered-450",
        "apim-stream-parallel3-450",
    ]:
        assert name in SCENARIOS
    assert SCENARIOS["apim-stream-parallel3-450"].parallel == 3
    assert SCENARIOS["apim-stream-buffered-450"].apim_variant == "buffered"


def test_build_request_urls_and_auth():
    st = Settings(
        mock_base_url="http://m:8000/",
        mock_api_key="k",
        apim_base_url="https://a.azure-api.net",
        apim_subscription_key="sub",
    )
    url, h = build_request(SCENARIOS["direct-silent-300"], st)
    assert url == "http://m:8000/silent" and h["x-mock-key"] == "k"
    url, h = build_request(SCENARIOS["apim-stream-buffered-450"], st)
    assert url == "https://a.azure-api.net/lab-buffered/stream"
    assert h["Ocp-Apim-Subscription-Key"] == "sub" and "x-mock-key" not in h


def test_results_template_header_matches_schema():
    from pathlib import Path

    header = (Path(__file__).parent.parent / "results" / "template.csv").read_text().strip()
    assert header.split(",") == CSV_COLUMNS


def test_csv_roundtrip_and_log_parsing(tmp_path):
    r = Result(run_id="r1", scenario="s", http_status=200, outcome="completed", total_s=1.5)
    out = tmp_path / "x.csv"
    write_csv(out, [r])
    write_csv(out, [r])  # append must not repeat the header
    rows = list(csv.DictReader(out.open()))
    assert len(rows) == 2 and list(rows[0]) == CSV_COLUMNS
    line = "2026-01-01T00:00:00Z RESULT " + json.dumps(r.row())
    assert parse_lines(["noise", line])[0]["scenario"] == "s"

"""Fake OpenAI Responses endpoint for offline tests. Test helper only: nothing deploys this.

POST /v1/responses  (stream on/off). Optional silence via the `x-fake-first-delay` header or
FIRST_DELAY: after the opening events (stream) or before the body (non-stream).
If tools are offered on the first turn the fake asks for one `ai_search` call; afterwards it answers.
"""

import asyncio
import json
import time
import uuid
from collections.abc import AsyncIterator

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse

app = FastAPI()
FIRST_DELAY = 0.0
FAKE_TEXT = '{"fake": true}'
FAKE_PLAN = json.dumps(
    {
        "engagement_id": "ENG-001",
        "sections": [
            {
                "section_id": "s1",
                "sheet_name": "Cover",
                "sheet_type": "cover",
                "owner_agent": "cover",
                "order": 1,
            },
            {
                "section_id": "s2",
                "sheet_name": "Firewall rules",
                "sheet_type": "firewall_rules",
                "owner_agent": "network",
                "order": 2,
            },
            {
                "section_id": "s3",
                "sheet_name": "Subnets",
                "sheet_type": "subnets",
                "owner_agent": "addressing",
                "order": 3,
            },
        ],
        "omitted_candidates": [
            {"sheet_name": "Compute", "reason": "no compute segments in the fake"}
        ],
        "warnings": [],
        "detected_vlans": [
            {"id": "100", "name": "Core", "cidr": "10.0.0.0/24", "platform": "onprem"}
        ],
    }
)
FAKE_SHEETS = json.dumps(
    {
        "sheets": [
            {
                "section_id": "s",
                "sheet_name": "Sheet",
                "columns": ["a", "b"],
                "rows": [["1", "2"]],
                "notes": "p1",
            }
        ],
        "issues": [],
    }
)


def _text_for(body: dict) -> str:
    probe = json.dumps(body)[:6000]
    if "planning agent" in probe:
        return FAKE_PLAN
    if "content agent" in probe:
        return FAKE_SHEETS
    return FAKE_TEXT


def _response(
    model: str, tool_call: bool, status: str = "completed", text: str = FAKE_TEXT
) -> dict:
    if tool_call:
        output: list[dict] = [
            {
                "type": "function_call",
                "id": "fc_1",
                "call_id": "call_1",
                "name": "ai_search",
                "arguments": '{"query": "vlan"}',
                "status": "completed",
            }
        ]
    else:
        output = [
            {
                "type": "message",
                "id": "msg_1",
                "role": "assistant",
                "status": "completed",
                "content": [{"type": "output_text", "text": text, "annotations": []}],
            }
        ]
    return {
        "id": f"resp_{uuid.uuid4().hex[:8]}",
        "object": "response",
        "created_at": int(time.time()),
        "status": status,
        "model": model,
        "output": output if status == "completed" else [],
        "usage": {
            "input_tokens": 11,
            "output_tokens": 7,
            "total_tokens": 18,
            "output_tokens_details": {"reasoning_tokens": 5},
            "input_tokens_details": {"cached_tokens": 0},
        },
        "parallel_tool_calls": True,
        "tool_choice": "auto",
        "tools": [],
        "metadata": {},
    }


def _sse(event: dict) -> bytes:
    return f"event: {event['type']}\ndata: {json.dumps(event)}\n\n".encode()


@app.post("/v1/responses")
async def responses(request: Request):
    body = await request.json()
    delay = float(request.headers.get("x-fake-first-delay", FIRST_DELAY))
    items = body.get("input") or []
    first_turn = not body.get("previous_response_id") and not any(
        isinstance(i, dict) and i.get("type") in ("function_call_output", "function_call")
        for i in items
    )
    tool_call = bool(body.get("tools")) and first_turn
    model = body.get("model", "fake")
    text = _text_for(body)
    headers = {"x-request-id": uuid.uuid4().hex}
    if not body.get("stream"):
        await asyncio.sleep(delay)
        return JSONResponse(_response(model, tool_call, text=text), headers=headers)

    async def gen() -> AsyncIterator[bytes]:
        final = _response(model, tool_call, text=text)
        started = {**final, "status": "in_progress", "output": []}
        yield _sse({"type": "response.created", "sequence_number": 0, "response": started})
        yield _sse({"type": "response.in_progress", "sequence_number": 1, "response": started})
        await asyncio.sleep(delay)  # "reasoning": connection open, nothing sent
        seq = 2

        def ev(type_: str, **kw) -> bytes:
            nonlocal seq
            seq += 1
            return _sse({"type": type_, "sequence_number": seq, **kw})

        item = final["output"][0]
        if tool_call:
            yield ev("response.output_item.added", output_index=0, item={**item, "arguments": ""})
            yield ev(
                "response.function_call_arguments.delta",
                item_id=item["id"],
                output_index=0,
                delta=item["arguments"],
            )
            yield ev(
                "response.function_call_arguments.done",
                item_id=item["id"],
                output_index=0,
                arguments=item["arguments"],
            )
            yield ev("response.output_item.done", output_index=0, item=item)
        else:
            empty = {**item, "status": "in_progress", "content": []}
            yield ev("response.output_item.added", output_index=0, item=empty)
            part = {"type": "output_text", "text": "", "annotations": []}
            yield ev(
                "response.content_part.added",
                item_id=item["id"],
                output_index=0,
                content_index=0,
                part=part,
            )
            for piece in (text[:7], text[7:]):
                yield ev(
                    "response.output_text.delta",
                    item_id=item["id"],
                    output_index=0,
                    content_index=0,
                    delta=piece,
                )
                await asyncio.sleep(0.05)
            yield ev(
                "response.output_text.done",
                item_id=item["id"],
                output_index=0,
                content_index=0,
                text=text,
            )
            yield ev(
                "response.content_part.done",
                item_id=item["id"],
                output_index=0,
                content_index=0,
                part={**part, "text": text},
            )
            yield ev("response.output_item.done", output_index=0, item=item)
        yield ev("response.completed", response=final)

    return StreamingResponse(gen(), media_type="text/event-stream", headers=headers)

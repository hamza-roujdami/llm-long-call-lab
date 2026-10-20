"""Worker settings (environment) and the per-run configuration chosen in the UI."""

from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FACTS = ROOT / "data" / "synthetic_docs" / "facts.jsonl"

# The three network paths under test.
Path3 = Literal["direct", "apim-default", "apim-stream"]
PATHS: tuple[Path3, ...] = ("direct", "apim-default", "apim-stream")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    run_id: str = ""
    store_mode: Literal["api", "memory"] = "api"
    run_config_json: str = ""  # memory mode only: config for a local run

    api_url: str = ""  # internal URL of the api, which holds run state
    internal_token: str = ""

    foundry_endpoint: str = ""  # https://<name>.openai.azure.com
    apim_url: str = ""  # https://<apim>.azure-api.net
    apim_key: str = ""
    model: str = "gpt-6-sol"  # Foundry deployment name
    search_endpoint: str = ""
    search_index: str = "design-pages"

    # Tests only: send every call to this OpenAI-compatible base URL (the fake model).
    llm_base_url_override: str = ""

    # Retry policy (pipeline mode). PLACEHOLDER defaults until the customer's real settings are known.
    # The matrix always uses a single attempt per call so every cut is visible.
    llm_max_attempts: int = 1
    llm_retry_backoff_s: float = 5.0
    llm_read_timeout_s: float = (
        3600.0  # longer than any scenario; the client must not be the limiter
    )

    facts_path: str = str(DEFAULT_FACTS)


class RunConfig(BaseModel):
    path: Path3 = "direct"
    stream: bool = True
    reasoning_effort: Literal["none", "minimal", "low", "medium", "high"] = "high"
    fact_tokens: int = (
        80_000  # facts[] size (chars/4 estimate); real tokens are ~1.25x, so 80K ~ 100K
    )
    section_fact_tokens: int = 20_000
    rounds: int = 1  # repeat the whole pipeline to stretch a run to 20-30 minutes
    max_tool_calls: int = 3  # per section agent
    max_output_tokens: int = 16_000
    depth: Literal["normal", "exhaustive"] = "normal"  # exhaustive: planner checks every fact
    agents: list[str] = ["cover", "network", "addressing", "compute"]
    note: str = ""

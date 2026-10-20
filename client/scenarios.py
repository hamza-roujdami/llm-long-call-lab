"""Named scenarios that map 1:1 to the run matrix in the README."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Scenario:
    name: str
    hypothesis: str
    target: str  # direct | apim
    endpoint: str  # silent | stream | gap
    params: dict[str, float] = field(default_factory=dict)
    client_stream: bool = True
    apim_variant: str = "stream"  # stream (buffer-response=false) | buffered (true)
    parallel: int = 1


SCENARIOS: dict[str, Scenario] = {
    s.name: s
    for s in [
        # Run matrix
        Scenario(
            "direct-silent-300", "H4", "direct", "silent", {"delay": 300}, client_stream=False
        ),
        Scenario(
            "direct-silent-450", "H4", "direct", "silent", {"delay": 450}, client_stream=False
        ),
        Scenario("apim-silent-300", "H1", "apim", "silent", {"delay": 300}, client_stream=False),
        Scenario("apim-stream-450", "H2", "apim", "stream", {"total": 450, "interval": 10}),
        Scenario("apim-gap-300", "H3", "apim", "gap", {"first": 10, "gap": 300, "then": 30}),
        Scenario(
            "apim-stream-buffered-450",
            "H2",
            "apim",
            "stream",
            {"total": 450, "interval": 10},
            apim_variant="buffered",
        ),
        Scenario(
            "apim-stream-parallel3-450",
            "H2",
            "apim",
            "stream",
            {"total": 450, "interval": 10},
            parallel=3,
        ),
        # Controls / boundary probes (optional)
        Scenario("direct-stream-450", "H4", "direct", "stream", {"total": 450, "interval": 10}),
        Scenario("apim-silent-200", "H1", "apim", "silent", {"delay": 200}, client_stream=False),
        Scenario("apim-gap-200", "H3", "apim", "gap", {"first": 10, "gap": 200, "then": 30}),
    ]
}

from src.agents import AGENT_MANIFEST
from src.skills import SKILL_MANIFEST
from src.tools import TOOL_MANIFEST

def test_capability_layers_are_explicit():
    assert len(AGENT_MANIFEST)>=5
    assert len(SKILL_MANIFEST)>=3
    assert len(TOOL_MANIFEST)>=2
    assert all(a["skills"] for a in AGENT_MANIFEST)

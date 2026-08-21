from src.agents import AGENT_MANIFEST,build_agents
from src.orchestrator import run_system
def test_team():
 a=build_agents();assert len(a)==5 and len({x.name for x in a})==5 and all(x["responsibility"] for x in AGENT_MANIFEST)
def test_trace():
 c={"matter":"m","decision_required":"d","stakeholders":["board"],"owner":"s","governance_documents":["c"],"controls":["r"],"evidence":[{"claim":"x","source":"c","status":"supplied"}]};r=run_system(c);assert r["trace"][0]["actor"]=="governance_orchestrator"

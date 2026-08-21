from .agents import build_agents
from .gates import evaluate_human_gate
from .state import RunState
SYSTEM_ID,SYSTEM_NAME,VERSION="F30","Agentic Corporate Governance","0.2.0"
def run_system(case,approve=False):
 s=RunState(case);s.record("governance_orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION})
 for a in build_agents():a.run(s)
 status=evaluate_human_gate(s,approve);s.record("governance_orchestrator","human authority gate evaluated",{"approve":approve,"status":status})
 return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"corporate_governance","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":"Resolve blockers before governance action." if status=="blocked" else "Evidence package is ready for authorized human review.","status":status,"trace":s.trace}

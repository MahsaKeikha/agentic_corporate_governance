from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List
from uuid import uuid4

SYSTEM_ID = "F30"
SYSTEM_NAME = "Agentic Corporate Governance"
VERSION = "0.1.0"

@dataclass
class State:
    case: Dict[str, Any]
    run_id: str = field(default_factory=lambda: str(uuid4()))
    analyses: Dict[str, Any] = field(default_factory=dict)
    evidence: List[Dict[str, str]] = field(default_factory=list)
    unresolved_questions: List[str] = field(default_factory=list)
    conflicts: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    trace: List[Dict[str, Any]] = field(default_factory=list)

    def record(self, actor: str, event: str, artifact: Any = None) -> None:
        self.trace.append({"step": len(self.trace) + 1, "actor": actor, "event": event, "artifact": artifact})

class Agent:
    name = "agent"
    def run(self, state: State) -> None:
        raise NotImplementedError

class GovernanceIntakeAgent(Agent):
    name = "governance_intake"
    def run(self, state: State) -> None:
        required = ["matter", "decision_required", "stakeholders"]
        missing = [key for key in required if not state.case.get(key)]
        state.analyses[self.name] = {"matter": state.case.get("matter"), "decision_required": state.case.get("decision_required"), "stakeholders": state.case.get("stakeholders", [])}
        state.unresolved_questions.extend(f"Missing required intake field: {key}" for key in missing)
        state.record(self.name, "structured governance intake", state.analyses[self.name])

class PolicyCharterAgent(Agent):
    name = "policy_charter"
    def run(self, state: State) -> None:
        docs = state.case.get("governance_documents", [])
        if not docs:
            state.unresolved_questions.append("No governance policy, charter, delegation, or equivalent authority evidence supplied")
        state.analyses[self.name] = {"documents_reviewed": docs, "authority_verified": bool(docs)}
        state.record(self.name, "reviewed supplied governance authority", state.analyses[self.name])

class RiskControlsAgent(Agent):
    name = "risk_controls"
    def run(self, state: State) -> None:
        declared = state.case.get("risks", [])
        state.risks.extend(declared)
        if not state.case.get("controls"):
            state.risks.append("Control evidence not supplied")
        state.analyses[self.name] = {"risks": list(state.risks), "controls": state.case.get("controls", [])}
        state.record(self.name, "assessed risks and controls", state.analyses[self.name])

class BoardProcessAgent(Agent):
    name = "board_process"
    def run(self, state: State) -> None:
        state.analyses[self.name] = {"agenda_item": state.case.get("matter"), "decision_required": state.case.get("decision_required"), "owner": state.case.get("owner"), "deadline": state.case.get("deadline")}
        if not state.case.get("owner"):
            state.unresolved_questions.append("Decision/action owner is not identified")
        state.record(self.name, "prepared board-process artifact", state.analyses[self.name])

class EvidenceAuditor(Agent):
    name = "evidence_auditor"
    def run(self, state: State) -> None:
        for item in state.case.get("evidence", []):
            state.evidence.append({"claim": str(item.get("claim", "")), "source": str(item.get("source", "")), "status": str(item.get("status", "supplied"))})
        conflicts = state.case.get("conflicts", [])
        state.conflicts.extend(conflicts)
        if not state.evidence:
            state.unresolved_questions.append("No material evidence supplied")
        state.analyses[self.name] = {"evidence_count": len(state.evidence), "conflicts": list(state.conflicts)}
        state.record(self.name, "audited evidence and conflicts", state.analyses[self.name])

AGENTS = [GovernanceIntakeAgent(), PolicyCharterAgent(), RiskControlsAgent(), BoardProcessAgent(), EvidenceAuditor()]

def run_system(case: Dict[str, Any], approve: bool = False) -> Dict[str, Any]:
    state = State(case=case)
    state.record("orchestrator", "run started", {"system_id": SYSTEM_ID, "version": VERSION})
    for agent in AGENTS:
        agent.run(state)
    blockers = bool(state.unresolved_questions or state.conflicts or state.risks)
    status = "approved_for_human_follow_through" if approve and not blockers else "blocked" if blockers else "awaiting_human_approval"
    recommendation = "Resolve blockers before governance action." if blockers else "Evidence package is ready for authorized human review."
    state.record("orchestrator", "human authority gate evaluated", {"approve": approve, "blockers": blockers, "status": status})
    return {"system_id": SYSTEM_ID, "system_name": SYSTEM_NAME, "version": VERSION, "run_id": state.run_id, "domain": "corporate_governance", "analyses": state.analyses, "evidence": state.evidence, "unresolved_questions": state.unresolved_questions, "conflicts": state.conflicts, "risks": state.risks, "recommendation": recommendation, "status": status, "trace": state.trace}

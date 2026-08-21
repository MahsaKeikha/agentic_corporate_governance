from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4
from .agents import build_agents

SYSTEM_ID = "F30"
SYSTEM_NAME = "Agentic Corporate Governance"
VERSION = "0.2.0"


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


def run_system(case: Dict[str, Any], approve: bool = False) -> Dict[str, Any]:
    state = State(case=case)
    state.record("governance_orchestrator", "run started", {"system_id": SYSTEM_ID, "version": VERSION})
    for agent in build_agents():
        agent.run(state)
    blockers = bool(state.unresolved_questions or state.conflicts or state.risks)
    status = "approved_for_human_follow_through" if approve and not blockers else "blocked" if blockers else "awaiting_human_approval"
    recommendation = "Resolve blockers before governance action." if blockers else "Evidence package is ready for authorized human review."
    state.record("governance_orchestrator", "human authority gate evaluated", {"approve": approve, "blockers": blockers, "status": status})
    return {
        "system_id": SYSTEM_ID,
        "system_name": SYSTEM_NAME,
        "version": VERSION,
        "run_id": state.run_id,
        "domain": "corporate_governance",
        "analyses": state.analyses,
        "evidence": state.evidence,
        "unresolved_questions": state.unresolved_questions,
        "conflicts": state.conflicts,
        "risks": state.risks,
        "recommendation": recommendation,
        "status": status,
        "trace": state.trace,
    }

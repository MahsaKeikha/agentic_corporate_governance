"""Specialist agents for F30 Agentic Corporate Governance."""
from typing import Any


class BaseAgent:
    name = "agent"
    responsibility = ""

    def run(self, state: Any) -> None:
        raise NotImplementedError


class GovernanceIntakeAgent(BaseAgent):
    name = "governance_intake"
    responsibility = "Normalize the matter, decision, stakeholders, ownership, and timing."

    def run(self, state: Any) -> None:
        required = ["matter", "decision_required", "stakeholders"]
        missing = [k for k in required if not state.case.get(k)]
        artifact = {
            "matter": state.case.get("matter"),
            "decision_required": state.case.get("decision_required"),
            "stakeholders": state.case.get("stakeholders", []),
            "owner": state.case.get("owner"),
            "deadline": state.case.get("deadline"),
        }
        state.analyses[self.name] = artifact
        state.unresolved_questions.extend(f"Missing required intake field: {k}" for k in missing)
        state.record(self.name, "structured governance intake", artifact)


class PolicyCharterAgent(BaseAgent):
    name = "policy_charter"
    responsibility = "Review supplied charters, policies, delegations, and authority evidence."

    def run(self, state: Any) -> None:
        docs = state.case.get("governance_documents", [])
        artifact = {"documents_reviewed": docs, "authority_verified": bool(docs)}
        if not docs:
            state.unresolved_questions.append("No governance authority evidence supplied")
        state.analyses[self.name] = artifact
        state.record(self.name, "reviewed governance authority", artifact)


class RiskControlsAgent(BaseAgent):
    name = "risk_controls"
    responsibility = "Review declared risks, controls, and unresolved control gaps."

    def run(self, state: Any) -> None:
        state.risks.extend(state.case.get("risks", []))
        controls = state.case.get("controls", [])
        if not controls:
            state.risks.append("Control evidence not supplied")
        artifact = {"risks": list(state.risks), "controls": controls}
        state.analyses[self.name] = artifact
        state.record(self.name, "assessed risks and controls", artifact)


class BoardProcessAgent(BaseAgent):
    name = "board_process"
    responsibility = "Prepare the board-process artifact, ownership, decision requirement, and deadline."

    def run(self, state: Any) -> None:
        artifact = {
            "agenda_item": state.case.get("matter"),
            "decision_required": state.case.get("decision_required"),
            "owner": state.case.get("owner"),
            "deadline": state.case.get("deadline"),
        }
        if not artifact["owner"]:
            state.unresolved_questions.append("Decision/action owner is not identified")
        state.analyses[self.name] = artifact
        state.record(self.name, "prepared board-process artifact", artifact)


class EvidenceAuditor(BaseAgent):
    name = "evidence_auditor"
    responsibility = "Audit provenance, missing evidence, and conflicts without inventing facts."

    def run(self, state: Any) -> None:
        for item in state.case.get("evidence", []):
            state.evidence.append({
                "claim": str(item.get("claim", "")),
                "source": str(item.get("source", "")),
                "status": str(item.get("status", "supplied")),
            })
        state.conflicts.extend(state.case.get("conflicts", []))
        if not state.evidence:
            state.unresolved_questions.append("No material evidence supplied")
        artifact = {"evidence_count": len(state.evidence), "conflicts": list(state.conflicts)}
        state.analyses[self.name] = artifact
        state.record(self.name, "audited evidence and conflicts", artifact)


def build_agents():
    return [GovernanceIntakeAgent(), PolicyCharterAgent(), RiskControlsAgent(), BoardProcessAgent(), EvidenceAuditor()]


AGENT_MANIFEST = [
    {"name": cls.name, "responsibility": cls.responsibility}
    for cls in [GovernanceIntakeAgent, PolicyCharterAgent, RiskControlsAgent, BoardProcessAgent, EvidenceAuditor]
]

from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class GovernanceIntakeAgent:
    name: str = "governance_intake_agent"
    responsibility: str = "Structure the governance matter, stakeholders, authority context, deadlines, and requested decision."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        required = ["matter", "decision_requested", "stakeholders"]
        missing = [k for k in required if not case.get(k)]
        return {"agent": self.name, "matter": case.get("matter"), "decision_requested": case.get("decision_requested"), "stakeholders": case.get("stakeholders", []), "missing": missing}

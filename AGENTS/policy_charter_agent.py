from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class PolicyCharterAgent:
    name: str = "policy_charter_agent"
    responsibility: str = "Map supplied policies, charters, delegations, and authority boundaries to the requested decision."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        policies = case.get("policies", [])
        delegations = case.get("delegations", [])
        return {"agent": self.name, "policy_count": len(policies), "delegation_count": len(delegations), "authority_evidence_present": bool(policies or delegations)}

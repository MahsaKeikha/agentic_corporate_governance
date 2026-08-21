from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class RiskControlsAgent:
    name: str = "risk_controls_agent"
    responsibility: str = "Identify governance risks, control gaps, dependencies, and escalation needs."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        risks: List[str] = list(case.get("risks", []))
        if not case.get("controls"):
            risks.append("No control evidence supplied")
        if case.get("conflicts"):
            risks.append("Potential conflict of interest requires review")
        return {"agent": self.name, "risks": risks, "blocked": bool(risks)}

from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class RiskRegister:
    risks: List[Dict[str, str]] = field(default_factory=list)

    def add(self, risk: str, severity: str = "medium", owner: str = "unassigned") -> Dict[str, str]:
        item = {"risk": risk, "severity": severity, "owner": owner}
        self.risks.append(item)
        return item

    def open_items(self) -> List[Dict[str, str]]:
        return list(self.risks)

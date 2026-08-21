from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class EvidenceAuditorAgent:
    name: str = "evidence_auditor_agent"
    responsibility: str = "Classify supplied, missing, conflicting, and unverified evidence and prevent unsupported clean handoff."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        evidence = list(case.get("evidence", []))
        missing: List[str] = list(case.get("missing_evidence", []))
        conflicts: List[str] = list(case.get("conflicting_evidence", []))
        return {"agent": self.name, "evidence_count": len(evidence), "missing": missing, "conflicts": conflicts, "clean": bool(evidence) and not missing and not conflicts}

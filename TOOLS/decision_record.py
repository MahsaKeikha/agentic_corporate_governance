from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict

@dataclass
class DecisionRecord:
    def create(self, decision: str, authority: str, rationale: str, evidence_refs: list[str]) -> Dict[str, Any]:
        return {
            "decision": decision,
            "authority": authority,
            "rationale": rationale,
            "evidence_refs": list(evidence_refs),
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }

from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class EvidenceLedger:
    entries: List[Dict[str, str]] = field(default_factory=list)

    def add(self, claim: str, source: str, status: str = "supplied") -> Dict[str, str]:
        entry = {"claim": claim, "source": source, "status": status}
        self.entries.append(entry)
        return entry

    def unresolved(self) -> List[Dict[str, str]]:
        return [e for e in self.entries if e["status"] in {"missing", "conflicting", "unverified"}]

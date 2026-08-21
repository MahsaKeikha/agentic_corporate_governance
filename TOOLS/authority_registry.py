from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

@dataclass
class AuthorityRegistry:
    def map(self, delegations: Iterable[Dict[str, Any]], action: str) -> List[Dict[str, Any]]:
        action_l = action.lower()
        return [d for d in delegations if action_l in str(d.get("scope", "")).lower()]

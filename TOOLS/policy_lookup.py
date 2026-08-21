from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

@dataclass
class PolicyLookup:
    def search(self, policies: Iterable[Dict[str, Any]], terms: Iterable[str]) -> List[Dict[str, Any]]:
        wanted = {t.lower() for t in terms}
        results = []
        for policy in policies:
            text = f"{policy.get('title','')} {policy.get('text','')}".lower()
            if any(term in text for term in wanted):
                results.append(policy)
        return results

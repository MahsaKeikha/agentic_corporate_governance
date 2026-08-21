from typing import Any, Dict, Iterable

def authority_mapping(case: Dict[str, Any], delegations: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    action = str(case.get("decision_requested", "")).lower()
    matches = [d for d in delegations if action and action in str(d.get("scope", "")).lower()]
    return {"action": action, "matching_delegations": matches, "authority_confirmed": bool(matches)}

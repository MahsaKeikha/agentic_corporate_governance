from typing import Any, Dict

def conflict_review(case: Dict[str, Any]) -> Dict[str, Any]:
    conflicts = list(case.get("conflicts", []))
    return {"conflicts": conflicts, "requires_recusal_or_review": bool(conflicts)}

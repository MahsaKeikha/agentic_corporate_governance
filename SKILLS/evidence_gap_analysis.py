from typing import Any, Dict, List

def evidence_gap_analysis(case: Dict[str, Any]) -> Dict[str, Any]:
    required = case.get("required_evidence", [])
    supplied = {str(x.get("id")) for x in case.get("evidence", []) if x.get("id") is not None}
    missing: List[str] = [str(r) for r in required if str(r) not in supplied]
    return {"required": list(required), "missing": missing, "complete": not missing}

from typing import Any, Dict, List

def governance_risk_assessment(case: Dict[str, Any]) -> Dict[str, Any]:
    risks: List[str] = list(case.get("risks", []))
    if not case.get("controls"):
        risks.append("Control evidence missing")
    if not case.get("decision_owner"):
        risks.append("Decision owner missing")
    return {"risks": risks, "requires_escalation": bool(risks)}

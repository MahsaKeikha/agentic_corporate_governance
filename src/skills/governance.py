def authority_mapping(documents):
    return {"documents_reviewed":documents,"authority_verified":bool(documents),"requires_human_interpretation":True}

def governance_risk_review(risks,controls):
    blockers=list(risks)
    if not controls:blockers.append("Control evidence not supplied")
    return {"declared_risks":list(risks),"controls":list(controls),"blockers":blockers}

def evidence_gap_analysis(record,required):
    return [f"Missing required field: {k}" for k in required if not record.get(k)]

SKILL_MANIFEST=["authority_mapping","governance_risk_review","evidence_gap_analysis"]

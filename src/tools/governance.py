def normalize_documents(documents):
    return [str(x).strip() for x in documents if str(x).strip()]

def build_decision_record(case):
    return {"agenda_item":case.get("matter"),"decision_required":case.get("decision_required"),"owner":case.get("owner"),"deadline":case.get("deadline"),"stakeholders":case.get("stakeholders",[])}

TOOL_MANIFEST=[
 {"name":"normalize_documents","kind":"deterministic","side_effects":False},
 {"name":"build_decision_record","kind":"deterministic","side_effects":False},
]

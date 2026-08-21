from src.system import run_system

def complete_case():
    return {
        "matter": "Approve partnership",
        "decision_required": "Board approval",
        "stakeholders": ["board"],
        "owner": "secretary",
        "governance_documents": ["charter"],
        "controls": ["conflict review"],
        "evidence": [{"claim": "approval required", "source": "charter", "status": "supplied"}],
    }

def test_complete_case_waits_for_human():
    result = run_system(complete_case())
    assert result["status"] == "awaiting_human_approval"
    assert len(result["trace"]) >= 7

def test_human_can_approve_clean_case():
    assert run_system(complete_case(), approve=True)["status"] == "approved_for_human_follow_through"

def test_approval_cannot_bypass_missing_evidence():
    case = complete_case()
    case["evidence"] = []
    result = run_system(case, approve=True)
    assert result["status"] == "blocked"
    assert result["unresolved_questions"]

def test_conflict_blocks_progression():
    case = complete_case()
    case["conflicts"] = ["Two supplied documents disagree on approval authority"]
    assert run_system(case, approve=True)["status"] == "blocked"

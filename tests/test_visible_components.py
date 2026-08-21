from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "AGENTS": ["governance_intake_agent.py", "policy_charter_agent.py", "risk_controls_agent.py", "board_process_agent.py", "evidence_auditor_agent.py"],
    "TOOLS": ["authority_registry.py", "policy_lookup.py", "evidence_ledger.py", "risk_register.py", "decision_record.py"],
    "SKILLS": ["authority_mapping.py", "governance_risk_assessment.py", "evidence_gap_analysis.py", "board_process_planning.py", "conflict_review.py"],
}

def test_visible_components_exist_and_compile():
    for folder, names in EXPECTED.items():
        for name in names:
            path = ROOT / folder / name
            assert path.exists(), path
            compile(path.read_text(), str(path), "exec")

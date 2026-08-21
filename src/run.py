import argparse
import json
from .system import run_system

EXAMPLE = {
    "matter": "Approve a strategic partnership framework",
    "decision_required": "Board approval of the proposed framework",
    "stakeholders": ["board", "CEO", "general counsel"],
    "owner": "corporate secretary",
    "deadline": "next board meeting",
    "governance_documents": ["board charter", "delegation of authority"],
    "controls": ["conflict disclosure review", "minutes and resolution review"],
    "evidence": [{"claim": "Board approval is required", "source": "delegation of authority", "status": "supplied"}]
}

def main():
    parser = argparse.ArgumentParser(description="Run F30 Agentic Corporate Governance")
    parser.add_argument("--example", action="store_true")
    parser.add_argument("--approve", action="store_true")
    args = parser.parse_args()
    case = EXAMPLE if args.example else {}
    print(json.dumps(run_system(case, approve=args.approve), indent=2))

if __name__ == "__main__":
    main()

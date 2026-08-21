# F30 Agentic Corporate Governance

Standalone multi-agent reference architecture for evidence-aware corporate governance preparation, board-process support, risk review, and decision traceability.

## Agent team

1. Governance Intake Agent
2. Policy and Charter Agent
3. Risk and Controls Agent
4. Board Process Agent
5. Evidence Auditor
6. Governance Orchestrator

## Engineering principles

This repository separates specialist responsibilities, preserves shared traceable state, records evidence provenance and unknowns, surfaces conflicts, and requires human authority before consequential action.

## Quick start

```bash
python -m src.run --example
pytest -q
```

The reference example is designed to run deterministically without a model API key.

## Output contract

Runs expose system/version identity, run ID, specialist analyses, evidence ledger, unresolved questions, conflicts, risks, recommendation, gate status, and execution trace.

## Authority boundary

This is decision-support software. It does not exercise fiduciary authority, provide legal certification, vote, execute resolutions, bind a corporation, or replace directors, officers, counsel, auditors, or qualified professionals.

## Maturity

**Reference implementation.** Production readiness requires organization-specific validation, security review, integration testing, governance approval, and operational evidence.

## AI Engineering Handbook Series

Companion books by Mahsa Keikha:

- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

## License

MIT.

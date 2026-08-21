# F30 Agentic Corporate Governance

Standalone multi-agent reference architecture for evidence-aware corporate governance preparation, board-process support, risk review, and decision traceability.

## Agent team

1. Governance Intake Agent
2. Policy and Charter Agent
3. Risk and Controls Agent
4. Board Process Agent
5. Evidence Auditor
6. Governance Orchestrator

The **actual specialist agent implementations live in [`src/agents.py`](src/agents.py)**. The orchestrated run state and human authority gate live in [`src/system.py`](src/system.py). Tests for both workflow behavior and agent composition live under [`tests/`](tests/).

## Architecture

```text
Case input
   ↓
Governance Intake Agent
   ↓
Policy & Charter Agent
   ↓
Risk & Controls Agent
   ↓
Board Process Agent
   ↓
Evidence Auditor
   ↓
Governance Orchestrator / Human Authority Gate
   ↓
Traceable result
```

Each agent has an explicit responsibility and writes an inspectable artifact into shared run state. The orchestrator does not erase missing evidence, conflicts, or risks when an approval flag is supplied.

## Quick start

```bash
python -m src.run --example
pytest -q
```

The reference example runs deterministically without a model API key.

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

# F30 Agentic Corporate Governance

Standalone multi-agent reference architecture for evidence-aware corporate governance preparation, board-process support, risk review, and decision traceability.

## Complete repository structure

```text
.github/workflows/tests.yml     CI across supported Python versions
src/agents.py                   specialist agent implementations and manifest
src/state.py                    shared typed run state
src/gates.py                    fail-closed human authority gate
src/orchestrator.py             multi-agent coordination and canonical result
src/system.py                   compatibility API
evals/evaluator.py              reference evaluator
examples/governance_case.json   reproducible offline fixture
benchmarks/README.md            domain benchmark contract
docs/ARCHITECTURE.md            architecture and workflow design
tests/                          system, agent, and architecture tests
SECURITY.md                     security and responsible-use policy
CONTRIBUTING.md                 contribution standard
CITATION.cff                    citation metadata
CHANGELOG.md                    release history
LICENSE                         MIT license
```

## Agent team

1. Governance Intake Agent
2. Policy and Charter Agent
3. Risk and Controls Agent
4. Board Process Agent
5. Evidence Auditor
6. Governance Orchestrator

The five specialists are executable roles. The Governance Orchestrator owns shared state, invokes the specialists, records the execution trace, and evaluates the human authority gate.

## Quick start

```bash
python -m src.run --example
pytest -q
```

## Authority boundary

This is decision-support software. It does not exercise fiduciary authority, provide legal certification, vote, execute resolutions, bind a corporation, or replace directors, officers, counsel, auditors, or qualified professionals.

## Maturity

**Reference implementation.** Production readiness requires organization-specific validation, security review, integration testing, governance approval, and operational evidence.

## AI Engineering Handbook Series

Companion books by Mahsa Keikha:

- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

MIT licensed.

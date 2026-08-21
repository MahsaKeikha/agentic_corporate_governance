# F30 Agentic Corporate Governance

Standalone multi-agent reference architecture for evidence-aware corporate governance preparation, board-process support, risk review, and decision traceability.

## Architecture

This repository exposes its capability layers directly:

```text
src/
├── agents/          specialist autonomous roles and manifest
├── tools/           deterministic callable capabilities
├── skills/          reusable governance reasoning procedures
├── memory/          run-scoped memory abstraction
├── schemas/         canonical contracts
├── prompts/         behavioral principles
├── config/          reference configuration
├── safety/          consequential-action policy
├── observability/   trace summaries
├── state.py         shared run state
├── gates.py         fail-closed approval gate
├── orchestrator.py  multi-agent coordination
├── system.py        public API
└── run.py           standalone CLI
```

### Agents
Governance Intake Agent, Policy and Charter Agent, Risk and Controls Agent, Board Process Agent, and Evidence Auditor, coordinated by the Governance Orchestrator.

### Skills
Authority mapping, governance risk review, and evidence-gap analysis.

### Tools
Document normalization and decision-record construction. Reference tools are deterministic and side-effect free.

See `docs/AGENTS_TOOLS_SKILLS.md` for the capability model.

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

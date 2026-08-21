# F30 Agents

The executable agent implementation lives in [`src/agents/`](../src/agents/). This root-level directory is the public agent catalog for the standalone system.

## Agent team
- Governance Intake Agent — structures matters, stakeholders, deadlines, and decision context.
- Policy & Charter Agent — analyzes supplied policies, charters, delegations, and authority boundaries.
- Risk & Controls Agent — surfaces governance risks, control gaps, and unresolved dependencies.
- Board Process Agent — prepares decision requirements, agenda dependencies, ownership, and follow-up.
- Evidence Auditor — separates supplied, missing, conflicting, and unverified evidence.
- Governance Orchestrator — coordinates the team while preserving human fiduciary authority.

See [`src/agents/team.py`](../src/agents/team.py) for executable specialists and [`src/orchestrator.py`](../src/orchestrator.py) for coordination.
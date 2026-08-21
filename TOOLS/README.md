# F30 Tools

The executable tool implementation lives in [`src/tools/`](../src/tools/).

The governance tool layer provides deterministic capabilities used by agents rather than hiding those operations inside prompts. It supports evidence/register inspection, authority and policy checks, risk/control analysis, and preparation of traceable governance artifacts.

Tools are intentionally separated from skills: tools perform operations; skills encode reusable domain procedures; agents decide when and how to apply both.

See [`src/tools/domain_tools.py`](../src/tools/domain_tools.py).
from typing import Any
from .base import BaseAgent
from ..skills import authority_mapping, governance_risk_review, evidence_gap_analysis
from ..tools import normalize_documents, build_decision_record

class GovernanceIntakeAgent(BaseAgent):
    name="governance_intake"; responsibility="Normalize the governance matter and decision context."; required_skills=("evidence_gap_analysis",); allowed_tools=("normalize_documents",)
    def run(self,s:Any)->None:
        a={"matter":s.case.get("matter"),"decision_required":s.case.get("decision_required"),"stakeholders":s.case.get("stakeholders",[]),"owner":s.case.get("owner"),"deadline":s.case.get("deadline")}
        s.analyses[self.name]=a
        for gap in evidence_gap_analysis(a,["matter","decision_required","stakeholders"]): s.unresolved_questions.append(gap)
        s.record(self.name,"structured governance intake",a)

class PolicyCharterAgent(BaseAgent):
    name="policy_charter"; responsibility="Map supplied policies, charters and delegated authority."; required_skills=("authority_mapping",); allowed_tools=("normalize_documents",)
    def run(self,s:Any)->None:
        docs=normalize_documents(s.case.get("governance_documents",[])); a=authority_mapping(docs); s.analyses[self.name]=a
        if not docs:s.unresolved_questions.append("No governance authority evidence supplied")
        s.record(self.name,"mapped governance authority",a)

class RiskControlsAgent(BaseAgent):
    name="risk_controls"; responsibility="Review governance risks and controls."; required_skills=("governance_risk_review",); allowed_tools=()
    def run(self,s:Any)->None:
        a=governance_risk_review(s.case.get("risks",[]),s.case.get("controls",[])); s.analyses[self.name]=a; s.risks.extend(a["blockers"]); s.record(self.name,"reviewed risks and controls",a)

class BoardProcessAgent(BaseAgent):
    name="board_process"; responsibility="Prepare a traceable human decision record."; required_skills=("authority_mapping",); allowed_tools=("build_decision_record",)
    def run(self,s:Any)->None:
        a=build_decision_record(s.case); s.analyses[self.name]=a
        if not a.get("owner"):s.unresolved_questions.append("Decision/action owner is not identified")
        s.record(self.name,"prepared board-process record",a)

class EvidenceAuditor(BaseAgent):
    name="evidence_auditor"; responsibility="Audit provenance, missing evidence and conflicts."; required_skills=("evidence_gap_analysis",); allowed_tools=()
    def run(self,s:Any)->None:
        for item in s.case.get("evidence",[]):s.evidence.append({"claim":str(item.get("claim","")),"source":str(item.get("source","")),"status":str(item.get("status","supplied"))})
        s.conflicts.extend(s.case.get("conflicts",[]))
        if not s.evidence:s.unresolved_questions.append("No material evidence supplied")
        a={"evidence_count":len(s.evidence),"conflicts":list(s.conflicts)};s.analyses[self.name]=a;s.record(self.name,"audited evidence",a)

CLASSES=[GovernanceIntakeAgent,PolicyCharterAgent,RiskControlsAgent,BoardProcessAgent,EvidenceAuditor]
def build_agents(): return [c() for c in CLASSES]
AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility,"skills":list(c.required_skills),"tools":list(c.allowed_tools)} for c in CLASSES]

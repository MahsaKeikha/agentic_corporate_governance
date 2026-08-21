def evaluate_result(r):
 keys=["system_id","version","analyses","evidence","unresolved_questions","conflicts","risks","status","trace"]
 m=[k for k in keys if k not in r]
 return {"schema_complete":not m,"missing_fields":m,"trace_steps":len(r.get("trace",[])),"blockers":len(r.get("unresolved_questions",[]))+len(r.get("conflicts",[]))+len(r.get("risks",[]))}

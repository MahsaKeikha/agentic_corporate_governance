def trace_summary(trace):
    return {"steps":len(trace),"actors":sorted({x.get("actor") for x in trace if x.get("actor")})}

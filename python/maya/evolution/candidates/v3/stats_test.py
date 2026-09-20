import json,sys
from pathlib import Path
F=Path("tasks.json")
q=json.loads(F.read_text()) if F.exists() else []
a=sys.argv[1:]
if a[:2]==["task","stats"]:
    done=sum(t.get("done",False) for t in q)
    print("Total",len(q),"Open",len(q)-done,"Done",done)
else:
    print("Candidate supports: task stats")

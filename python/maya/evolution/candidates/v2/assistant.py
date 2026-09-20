import json,sys
from pathlib import Path
from datetime import datetime
F=Path("tasks.json")
q=json.loads(F.read_text()) if F.exists() else []
a=sys.argv[1:]
if a[:2]==["task","list"]:
    [print(i,t["text"],"[done]" if t["done"] else "[open]",("due: "+t["due"] if t.get("due") else "")) for i,t in enumerate(q,1)]
elif a[:2]==["task","add"] and len(a)>2:
    q.append({"text":" ".join(a[2:]),"done":False,"created":datetime.now().strftime("%Y-%m-%d %H:%M")})
    F.write_text(json.dumps(q, indent=2))
    print("Added task",len(q))
elif a[:2]==["task","done"] and len(a)>2:
    F.write_text(json.dumps(q, indent=2))
elif a[:2]==["task","remove"] and len(a)>2:
    F.write_text(json.dumps(q, indent=2))
else:
    print("Usage: python3 assistant.py task list")
    print("Usage: python3 assistant.py task add TEXT")
    print("Usage: python3 assistant.py task done NUMBER")
    print("Usage: python3 assistant.py task remove NUMBER")

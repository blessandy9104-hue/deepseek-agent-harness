import json, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
PROPOSALS = ROOT / "evolution/3d_proposals"

def files():
    return sorted(PROPOSALS.glob("3d-*.json"))

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

command = sys.argv[1].lower() if len(sys.argv) > 1 else "list"
if command == "list":
    for path in files():
        item = load(path)
        print(f"{item['proposal_id']} | {item['approval_status']} | {item['requested_result']}")
elif command in {"approve", "reject"} and len(sys.argv) == 3:
    matches = [p for p in files() if load(p).get("proposal_id") == sys.argv[2]]
    if not matches:
        raise SystemExit("Proposal not found")
    path = matches[0]
    item = load(path)
    item["approval_status"] = "approved_for_simulation" if command == "approve" else "rejected"
    item["reviewed_at"] = datetime.now(timezone.utc).isoformat()
    item["reviewed_by"] = "Andy"
    item["execution_mode"] = "simulation_only"
    item["live_bridge_enabled"] = False
    path.write_text(json.dumps(item, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(item, indent=2))
    print("No live Autodesk Maya operation was performed.")
else:
    raise SystemExit("Usage: python3 maya_3d_review.py [list|approve PROPOSAL_ID|reject PROPOSAL_ID]")

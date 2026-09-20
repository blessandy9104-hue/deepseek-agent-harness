import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "evolution/3d_proposals"
POLICY = ROOT / "knowledge/cooperation_policy.json"

if len(sys.argv) < 2:
    print("Usage: python3 maya_3d_propose.py <ordinary English 3D request>")
    raise SystemExit(2)

request = " ".join(sys.argv[1:]).strip()
text = request.lower()
objects = []
if "cube" in text:
    objects.append("one cube")
if "sphere" in text:
    objects.append("one sphere")
if "chair" in text:
    objects.append("chair components")
if not objects:
    objects.append("objects to be determined during review")

operation = "Prepare a simulation-only Autodesk Maya scene plan for: " + request
if "delete" in text or "remove" in text:
    operation = "Prepare a reversible deletion plan for: " + request

proposal = {
    "proposal_id": datetime.now(timezone.utc).strftime("3d-%Y%m%dT%H%M%SZ"),
    "created_at": datetime.now(timezone.utc).isoformat(),
    "requested_by": "Andy",
    "requested_result": request,
    "affected_objects": objects,
    "proposed_operation": operation,
    "execution_mode": "simulation_only",
    "generated_script": None,
    "risk": "low for simulation; no live scene changes are permitted",
    "approval_status": "pending",
    "rollback_plan": "No live change has occurred. Delete this proposal to discard it.",
    "live_bridge_enabled": False,
    "policy_file": str(POLICY),
}
path = OUT / (proposal["proposal_id"] + ".json")
path.write_text(json.dumps(proposal, indent=2) + "\n", encoding="utf-8")
print(json.dumps(proposal, indent=2))
print(f"Saved simulation proposal: {path}")

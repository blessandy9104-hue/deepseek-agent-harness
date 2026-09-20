import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROFILE = ROOT / "andy_profile.json"


def load():
    return json.loads(PROFILE.read_text(encoding="utf-8"))


def save(data):
    PROFILE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def now():
    return datetime.now(timezone.utc).isoformat()


def show(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))


def propose(data, category, key, value, confidence, evidence):
    item = {
        "category": category,
        "key": key,
        "value": value,
        "confidence": float(confidence),
        "evidence": evidence,
        "status": "pending_review",
        "created_at": now()
    }
    data.setdefault("inferred_preferences_pending_review", []).append(item)
    save(data)
    print("INFERENCE STORED FOR REVIEW")
    print(json.dumps(item, indent=2, ensure_ascii=False))


def approve(data, index):
    pending = data.setdefault("inferred_preferences_pending_review", [])
    item = pending.pop(index)
    item["status"] = "approved"
    item["approved_at"] = now()
    category = data.setdefault(item["category"], {})
    category[item["key"]] = item
    save(data)
    print("PREFERENCE APPROVED")
    print(json.dumps(item, indent=2, ensure_ascii=False))


def reject(data, index):
    pending = data.setdefault("inferred_preferences_pending_review", [])
    item = pending.pop(index)
    item["status"] = "rejected"
    item["rejected_at"] = now()
    data.setdefault("rejected_inferences", []).append(item)
    save(data)
    print("INFERENCE REJECTED")
    print(json.dumps(item, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    data = load()
    args = sys.argv[1:]
    if not args or args[0] == "show":
        show(data)
    elif args[0] == "propose" and len(args) >= 6:
        propose(data, args[1], args[2], args[3], args[4], " ".join(args[5:]))
    elif args[0] == "approve" and len(args) == 2:
        approve(data, int(args[1]))
    elif args[0] == "reject" and len(args) == 2:
        reject(data, int(args[1]))
    else:
        print("Usage:")
        print("  python3 andy_profile.py show")
        print("  python3 andy_profile.py propose CATEGORY KEY VALUE CONFIDENCE EVIDENCE")
        print("  python3 andy_profile.py approve INDEX")
        print("  python3 andy_profile.py reject INDEX")
        raise SystemExit(1)

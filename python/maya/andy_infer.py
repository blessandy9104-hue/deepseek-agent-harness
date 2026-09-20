import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "andy_evidence.jsonl"
PROFILE = ROOT / "andy_profile.json"


def load_profile():
    return json.loads(PROFILE.read_text(encoding="utf-8"))


def save_profile(data):
    PROFILE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def infer():
    groups = defaultdict(list)
    if EVIDENCE.exists():
        for line in EVIDENCE.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            if item.get("approved") is True:
                key = (item["category"], item["key"], item["value"])
                groups[key].append(item)

    profile = load_profile()
    pending = profile.setdefault("inferred_preferences_pending_review", [])
    existing = {(x.get("category"), x.get("key"), x.get("value")) for x in pending}

    created = 0
    for (category, key, value), items in groups.items():
        if (category, key, value) in existing:
            continue
        confidence = min(0.50 + 0.15 * (len(items) - 1), 0.95)
        pending.append({
            "category": category,
            "key": key,
            "value": value,
            "confidence": round(confidence, 2),
            "evidence": [item.get("observation", "") for item in items],
            "status": "pending_review",
            "source_count": len(items)
        })
        created += 1

    save_profile(profile)
    print(f"NEW INFERENCES FOR REVIEW: {created}")
    print(f"APPROVED EVIDENCE GROUPS: {len(groups)}")


if __name__ == "__main__":
    infer()

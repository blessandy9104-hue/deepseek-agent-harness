import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "andy_decisions.jsonl"

records = []
for line in LEDGER.read_text(encoding="utf-8").splitlines():
    if line.strip():
        item = json.loads(line)
        if item.get("approved") is True:
            records.append(item)

groups = defaultdict(list)
for item in records:
    groups[item.get("decision_type", "unknown")].append(item)

print(f"APPROVED DECISIONS: {len(records)}")
for decision_type, items in groups.items():
    choices = Counter(item.get("choice") for item in items)
    print(f"{decision_type}: {len(items)} example(s)")
    print(f"choices: {dict(choices)}")
    if len(items) < 2:
        print("pattern status: INSUFFICIENT EVIDENCE")
    else:
        print("pattern status: REVIEW REQUIRED")
        print("pattern candidate: compare repeated choices and stated reasons before inferring a preference")

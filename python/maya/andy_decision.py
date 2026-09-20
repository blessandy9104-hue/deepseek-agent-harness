import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "andy_decisions.jsonl"


def now():
    return datetime.now(timezone.utc).isoformat()


def record(decision_type, choice, alternatives, reason, *, features=None,
           primary=None, secondary=None, context=None, current=None,
           alpha=None):
    """Record a decision. When the optional priority/confidence signals are
    supplied (``features`` plus ``primary``/``secondary``/``context``), the
    decision's priority, fused signal, and confidence are computed and
    validated by the Math Coordination Agent — priority from normalized
    vectors, fusion through ``rig_math.blend_pose``, confidence stabilized by
    ``exp_smooth``. No heuristic arithmetic is used."""
    item = {
        "decision_type": decision_type,
        "choice": choice,
        "alternatives_considered": alternatives,
        "reason": reason,
        "approved": True,
        "recorded_at": now()
    }
    if primary is not None and secondary is not None and context is not None:
        from maya_identity.wireframe.math_coordinator import (
            MATH_AGENT, TASK_PRIORITY_REFERENCE)
        decision = MATH_AGENT.task_decision(
            features if features is not None else TASK_PRIORITY_REFERENCE,
            primary=primary, secondary=secondary, context=context,
            current=current, alpha=alpha)
        validated = MATH_AGENT.task_decision_ok(decision)
        item["priority"] = decision["priority"]
        item["confidence"] = decision["confidence"]
        item["fused"] = decision["fused"]
        item["task_decision_ok"] = validated["ok"]
    with LEDGER.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    print("DECISION RECORDED")
    print(json.dumps(item, indent=2, ensure_ascii=False))


def show():
    if not LEDGER.exists():
        print("No decisions recorded.")
        return
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if line.strip():
            print(json.dumps(json.loads(line), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "show":
        show()
    elif args[0] == "record" and len(args) >= 5:
        record(args[1], args[2], args[3].split("|"), " ".join(args[4:]))
    else:
        print("Usage:")
        print("  python3 andy_decision.py show")
        print("  python3 andy_decision.py record TYPE CHOICE ALT1|ALT2 REASON")
        raise SystemExit(1)

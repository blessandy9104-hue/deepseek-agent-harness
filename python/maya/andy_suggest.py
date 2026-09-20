import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROFILE = ROOT / "andy_profile.json"


def approved_interests():
    data = json.loads(PROFILE.read_text(encoding="utf-8"))
    interests = data.get("interests", {})
    return [item for item in interests.values() if item.get("status") == "approved"]


def suggest():
    interests = approved_interests()
    if not interests:
        print("No approved interests available yet.")
        return

    print("Personalized suggestions for Andy:")
    for item in interests:
        value = item.get("value", "")
        key = item.get("key", "")
        if key == "self_evolution":
            suggestion = "Continue improving Maya through sandboxed experiments, behavioral tests, approval gates, and rollback."
        elif key == "philosophy":
            suggestion = "Build a philosophy learning track and connect new readings to Maya’s approved knowledge system."
        else:
            suggestion = f"Explore the approved interest: {value}."
        print(f"- {key}: {suggestion}")
        print(f"  basis: confidence {item.get('confidence')}, status {item.get('status')}")


if __name__ == "__main__":
    suggest()

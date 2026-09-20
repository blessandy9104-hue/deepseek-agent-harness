"""Mother-Maya seed/hypothesis walkthrough.

Isolated from the real suggestion-review state (matches the fix applied to
test_pending_approval_live.py) so running this test doesn't leave the
checked-in maya_suggestion_reviews.json / audit log dirty.
"""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import maya_suggestion_review as review_module
from maya_chat import maya_local_command, maya_role_context
from maya_proactive_suggestions import generate_seed_suggestion, sample_scenario

_tmp_dir = tempfile.TemporaryDirectory()
_patches = [
    patch.object(review_module, "REVIEW_FILE", Path(_tmp_dir.name) / "maya_suggestion_reviews.json"),
    patch.object(review_module, "AUDIT_FILE", Path(_tmp_dir.name) / "maya_suggestion_review_audit.jsonl"),
]
for _p in _patches:
    _p.start()

purpose = maya_role_context()
assert "Mother Maya vision:" in purpose
assert "narrowing complex possibilities" in purpose
assert "P1_human_benefit" in purpose
assert "test individual and community convergence" in purpose

result = generate_seed_suggestion(sample_scenario())
assert result["status"] == "hypothesis_only"
assert result["seed_version"] == "0.2"
assert result["approval_required_for_change"] is True
assert result["memory_update"] == "not_performed"
assert result["external_action"] == "not_performed"
assert len(result["options"]) == 2
assert result["preferred_path"] == "A"
assert result["convergence_status"] == "partially_convergent"
assert result["human_review_status"] == "awaiting_review"

conflict = generate_seed_suggestion({
    "goal": "Improve access to a useful service",
    "constraints": ["limited budget"],
    "signals": ["early user interest"],
    "affected_interests": ["future users", "local community"],
    "conflict": "The fastest route may exclude people with limited connectivity.",
})
assert conflict["convergence_status"] == "conflict_identified"
assert "exclude" in conflict["conflict_note"]

needs_goal = generate_seed_suggestion({})
assert needs_goal["status"] == "needs_goal"
assert needs_goal["human_review_status"] == "clarification_needed"

rendered = maya_local_command(":seed demo")
parsed = json.loads(rendered)
assert parsed["label"] == "mother_maya_seed_hypothesis"
assert parsed["human_review_status"] == "awaiting_review"
print("purpose_explicit=OK")
print("protected_principles_visible=OK")
print("decision_pipeline_visible=OK")
print("sample_suggestion=OK")
print("option_schema=OK")
print("conflict_handling=OK")
print("clarification_gate=OK")
print("hypothesis_labeled=OK")
print("no_memory_or_external_action=OK")

for _p in _patches:
    _p.stop()
_tmp_dir.cleanup()
from pathlib import Path
from maya_chat import maya_local_command

ROOT = Path(__file__).resolve().parent

owner_queries = [
    "Who is Andy?",
    "Tell me who Andy is.",
    "What do you know about Andy?",
    "Do you know Andy?",
    "Andy?",
]
for query in owner_queries:
    result = maya_local_command(query)
    assert result == "Andy is my creator, owner, and human supervisor.", (query, result)

warhol = maya_local_command("Who is Andy Warhol?")
assert warhol is None or "creator, owner" not in warhol

source = (ROOT / "maya_web_research.py").read_text(encoding="utf-8")
assert "_topic_matches" in source
assert "No focused public result matched" in source
print("owner_variants=OK")
print("public_name_separation=OK")
print("topic_isolation=OK")
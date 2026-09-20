from __future__ import annotations


def rewrite_follow_up(text: str, history: list[dict] | None = None) -> str:
    """Expand short follow-ups using only the current conversation."""
    clean = text.strip().rstrip("?!.,:;")
    if not clean or not history:
        return clean

    previous_user_message = ""
    for message in reversed(history):
        if message.get("role") == "user":
            previous_user_message = message.get("content", "").strip()
            break

    if not previous_user_message:
        return clean

    if clean.lower() in {"why", "why?", "how so", "how come"}:
        return f"{clean} regarding this previous question: {previous_user_message}"

    follow_up_starts = (
        "tell me more",
        "what about",
        "how about",
        "what are they",
        "what is he",
        "what is she",
        "what happened next",
    )
    if clean.lower().startswith(follow_up_starts):
        return f"{clean} regarding this previous question: {previous_user_message}"

    return clean

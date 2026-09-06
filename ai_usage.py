import os

import anthropic

_client = None


def _get_client() -> anthropic.Anthropic:
    """Create the client on first use, not at import time."""
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set")
        _client = anthropic.Anthropic(api_key=api_key)
    return _client


def give_interaction_safety_rating(med):
    message = _get_client().messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="Answer with a single number only",
        messages=[
            {"role": "user", "content": f"Rate the pharmacological safety of combining psilocybin and {med}, from 1 to 10. Answer only with this number."},
        ],
    )

    try:
        return int(message.content[0].text.strip())
    except (ValueError, IndexError):
        return None


def give_interaction_safety_text(med):
    message = _get_client().messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system="Give a short and concise answer. No Titles, just plain text, 1-3 sentences",
        messages=[
            {"role": "user", "content": f"Rate the pharmacological safety of combining psilocybin and {med}, answer with a **short** text of 2-3 sentences. No titles, just plain text. Use language for normal people."},
        ],
    )

    return message.content[0].text


if __name__ == "__main__":
    print(give_interaction_safety_text("lithium"))
    print(give_interaction_safety_rating("lithium"))
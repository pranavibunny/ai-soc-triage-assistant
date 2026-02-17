def sanitize_text(text):
    suspicious_patterns = [
        "ignore previous instructions",
        "reveal system prompt",
        "execute this command",
        "you are now",
    ]

    cleaned = text.lower()

    for pattern in suspicious_patterns:
        cleaned = cleaned.replace(pattern, "[REMOVED]")

    return cleaned

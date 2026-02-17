def clean_json_text(text):
    text = text.strip()

    # Remove markdown blocks
    text = text.replace("```json", "")
    text = text.replace("```", "")

    # Auto-fix missing closing brace
    if text.count("{") > text.count("}"):
        text += "}"

    return text.strip()

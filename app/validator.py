def validate_output(response):
    blocked_words = [
        "rm -rf",
        "powershell -enc",
        "download",
        "curl http",
    ]

    lower_resp = response.lower()

    for word in blocked_words:
        if word in lower_resp:
            return False, "Unsafe output detected"

    return True, "Output safe"

import ollama
from config import SYSTEM_PROMPT

def analyze_alert(alert_text):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": alert_text},
        ],
    )

    return response["message"]["content"]

def repair_json(bad_output):
    repair_prompt = f"""
Convert the following response into VALID JSON ONLY.
Do not add explanations or extra text.

Response:
{bad_output}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": repair_prompt}
        ],
    )

    return response["message"]["content"]


def map_to_mitre(alert_text):
    text = alert_text.lower()

    if "powershell" in text:
        return {
            "technique_id": "T1059.001",
            "technique_name": "PowerShell",
            "tactic": "Execution"
        }

    if "cmd.exe" in text:
        return {
            "technique_id": "T1059.003",
            "technique_name": "Windows Command Shell",
            "tactic": "Execution"
        }

    return {
        "technique_id": "Unknown",
        "technique_name": "Unknown",
        "tactic": "Unknown"
    }

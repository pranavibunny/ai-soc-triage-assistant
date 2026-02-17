import json
from sanitizer import sanitize_text
from validator import validate_output
from mitre_mapper import map_to_mitre
from agent import analyze_alert, repair_json
from json_utils import clean_json_text



with open("data/sample_alerts.json", "r") as f:
    alerts = json.load(f)

for alert in alerts:
    print("\n--- NEW ALERT ---")

    raw_text = str(alert)

    # Step 1: sanitize input
    safe_input = sanitize_text(raw_text)

    # Step 2: AI analysis
    ai_response = analyze_alert(safe_input)

    # Step 3: validate output
    is_safe, msg = validate_output(ai_response)

    if not is_safe:
        print("Blocked:", msg)
        continue

    # Step 4: Try parsing JSON
    try:
        cleaned_response = clean_json_text(ai_response)
        parsed = json.loads(cleaned_response)

        print("Severity:", parsed["severity"])
        print("Risk Score:", parsed["risk_score"])
        focus = parsed["investigation_focus"]
        if focus == "parent_process":
            print("🔎 AGENT ACTION: Gather parent process details")
        elif focus == "network_activity":
            print("🌐 AGENT ACTION: Check network connections")
        else:
            print("✅ No additional investigation needed")

        print("Reason:", parsed["reason"])
        print("Next Steps:", parsed["recommended_steps"])

        # Agent decision logic
        if risk >= 85:
            print("🚨 HIGH RISK — Escalate")
        elif risk >= 60:
            print("⚠️ INVESTIGATE")
        else:
            print("✅ Monitor")
        
        mitre = map_to_mitre(raw_text)
        print("MITRE Technique:", mitre["technique_id"])
        print("Technique Name:", mitre["technique_name"])
    
    except:
        print("AI returned invalid JSON — attempting repair...")
        fixed_response = repair_json(ai_response)
        
        try:
            parsed = json.loads(fixed_response)
            print("✅ JSON repaired successfully")
            print(parsed)
            
        except:
            print("❌ Repair failed")
            print(ai_response)



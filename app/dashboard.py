import streamlit as st
import json
from sanitizer import sanitize_text
from agent import analyze_alert, repair_json
from mitre_mapper import map_to_mitre
from json_utils import clean_json_text

##UI Helper##

def render_analysis(parsed, raw_text, alert):
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Severity", parsed["severity"])
    with col2:
        st.metric("Risk Score", parsed["risk_score"])

    if parsed["risk_score"] >= 80:
        st.error("🚨 HIGH RISK — Escalate Immediately")
    elif parsed["risk_score"] >= 50:
        st.warning("⚠️ MEDIUM RISK — Investigate")
    else:
        st.success("✅ LOW RISK — Monitor")

    st.write("### 🧠 Reason:")
    st.write(parsed["reason"])

    st.write("### 🔎 Recommended Steps:")
    for step in parsed["recommended_steps"]:
        st.write(f"- {step}")

    st.write("### 🤖 Agent Investigation Focus:")
    focus = parsed.get("investigation_focus", "none")
    st.info(f"🔎 Agent suggests: {focus}")

    mitre = map_to_mitre(raw_text)

    st.write("### 🎯 MITRE ATT&CK Mapping")
    c1, c2, c3 = st.columns(3)
    c1.metric("Technique ID", mitre["technique_id"])
    c2.metric("Technique", mitre["technique_name"])
    c3.metric("Tactic", mitre["tactic"])

    with st.expander("View Raw Alert"):
        st.json(alert)


##Main##

st.title("AI SOC Triage Assistant")

uploaded = st.file_uploader("Upload alert JSON", type="json")

if uploaded:
    alerts = json.load(uploaded)

    for alert in alerts:
        with st.container():
            st.subheader("🚨 New Alert")


        raw_text = str(alert)

        safe_input = sanitize_text(raw_text)

        st.caption("🔐 Input sanitized before AI analysis (prompt-injection protection).")

        ai_response = analyze_alert(safe_input)

        st.write("### AI Analysis")

        
        # ALWAYS clean first
        cleaned_response = clean_json_text(ai_response)
        
        try:
            # First parse attempt (after cleaning)
            parsed = json.loads(cleaned_response)
        except Exception:
            st.warning("AI response needed repair — attempting fix...")
            repaired = repair_json(cleaned_response)
            repaired = clean_json_text(repaired)
            try:
                parsed = json.loads(repaired)
                st.success("✅ JSON repaired successfully")
            except Exception as e:
                st.error(f"❌ Final parsing failed: {e}")
                st.code(ai_response)
                continue
                
        # ONLY run if parsing succeeded
        render_analysis(parsed, raw_text, alert)





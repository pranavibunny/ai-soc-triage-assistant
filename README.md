# 🛡 AI SOC Triage Assistant

An AI-assisted security analyst prototype built to explore how Generative AI can help Security Operations Center (SOC) workflows while keeping safety and control in deterministic code.

This project combines cybersecurity thinking with practical GenAI engineering.

---

## 🌍 Why This Project Exists

Security teams receive large numbers of endpoint alerts every day.

Real-world challenges include:

- 🚨 Alert fatigue — too many alerts to investigate manually
- ⏱ Slow investigations — analysts must gather context before deciding risk
- 🧠 Inconsistent analysis — results depend on analyst experience
- 📉 Limited explanation from traditional tooling

Modern security tools detect suspicious activity, but analysts still spend time understanding **why** something is risky and what to investigate next.

Generative AI can help with reasoning — but AI alone introduces new risks such as:

- prompt injection
- inconsistent output formats
- hallucinated recommendations
- unsafe automation

---

## 🎯 Project Goal

Build a safe AI assistant that helps analysts triage alerts without giving AI direct control over security actions.

Core design idea:

AI assists reasoning
Code enforces safety
Human makes final decisions


---

## 🧠 What This Project Does

### 🤖 AI Alert Analysis

A local language model analyzes endpoint-style alerts and returns:

- Severity (Low / Medium / High)
- Risk score
- Reasoning explanation
- Investigation recommendations

---

### 🔐 Security Guardrails (Important)

Instead of trusting AI blindly, this project adds multiple safety layers:

- Input sanitization (reduces prompt injection risk)
- Output validation before decisions
- Structured JSON parsing
- Self-repair loop if AI output formatting fails

This follows a **zero-trust approach to AI output**.

---

### ⚙️ Deterministic Decision Logic

AI suggests risk, but code controls actions.

Example:

If risk_score >= 80 → escalate
Else → investigate or monitor
This keeps behavior predictable and safe.

---

### 🎯 MITRE ATT&CK Mapping
Alerts are enriched with MITRE ATT&CK techniques to provide attacker-behavior context.

### 🤖 Agent-Inspired Workflow
The AI can suggest what should be investigated next, such as:

parent process lineage

network activity

This mimics how real SOC analysts gather additional context before final decisions.

---

### 🖥 Streamlit Dashboard
The project includes an interactive dashboard showing:

Risk score and severity
AI reasoning
Recommended investigation steps
MITRE ATT&CK context
Raw alert details

---

### 🏗 Architecture Overview
Alert Input
   ↓
Input Sanitizer
   ↓
LLM Analysis (local model)
   ↓
JSON Validation
   ↓
Self-Repair Loop (if needed)
   ↓
Deterministic Risk Logic
   ↓
Streamlit Dashboard

---

### 🔐 Security Design Principles Demonstrated
Treat AI output as untrusted input
Separate reasoning from enforcement
Use deterministic logic for decisions
Avoid direct AI-driven automation

---

### 🧪 Example Scenario
Example alert:

winword.exe → powershell.exe → encoded command
AI may identify this as:

High risk execution behavior

Possible abuse of scripting tools

Recommendation: investigate parent process and network activity

---

## 📸 Dashboard Preview

![Dashboard](screenshots/dashboard.png)

---

### 🖥 Tech Stack
Python 3.11
Streamlit
Ollama (local LLM runtime)
JSON parsing & validation

---

## ⚡ Quick Start

```bash
pip install -r requirements.txt
ollama run llama3
streamlit run app/dashboard.py
```
---

## ▶️ How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start local model
ollama run llama3

3️⃣ Launch dashboard
streamlit run app/dashboard.py


---

## 📚 What I Learned From This Project
LLM outputs are probabilistic, not deterministic
AI outputs must be validated before automation
Prompt injection can occur even through log data
Structured outputs are required for safe workflows
Agent-like systems require multi-step reasoning


---

## 📈 Future Improvements
Multi-step investigation loop (true agent workflow)
AI-based prompt injection detection
More advanced MITRE reasoning
Alert prioritization and queueing
Confidence calibration for risk scoring


---

## ⚠️ Disclaimer
This project uses synthetic alerts and is intended for learning and portfolio purposes only.


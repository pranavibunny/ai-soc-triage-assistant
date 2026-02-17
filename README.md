# AI SOC Triage Assistant

A security-focused AI assistant that helps triage endpoint alerts using a local LLM with safety guardrails.

---

## 🚨 Problem

Security analysts face alert fatigue and inconsistent investigations.  
This project explores how GenAI can assist SOC workflows while maintaining security controls.

---

## 🎯 Features

- AI-based alert analysis (local LLM via Ollama)
- Risk scoring and severity estimation
- Prompt-injection input sanitization
- Output validation and JSON repair loop
- MITRE ATT&CK mapping
- Agent-style investigation guidance
- Streamlit dashboard UI

---

## 🏗 Architecture

Alert Input  
→ Sanitizer (Zero Trust Input)  
→ AI Analyst  
→ JSON Validation  
→ Self-Repair Loop  
→ Risk Decision Logic  
→ Streamlit Dashboard

---

## 🔐 Security Controls

- Input sanitization to reduce prompt injection risk
- Output validation before decisions
- Deterministic risk-based escalation logic
- Local model (no cloud data exposure)

---

## 🤖 Agentic Elements

- Investigation focus suggestion
- Multi-step workflow readiness
- AI self-correction for invalid outputs

---

## 🖥 Tech Stack

- Python
- Streamlit
- Ollama (Llama3 local model)
- JSON handling

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt

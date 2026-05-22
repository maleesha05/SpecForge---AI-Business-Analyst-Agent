# ◈ SpecForge — AI Business Analyst Agent

> Turn a client conversation into a professional Functional Specification Document in minutes — powered by AI.

---

## 🎯 The Problem I Solved

Requirements gathering is one of the most time-consuming parts of software development. Business Analysts spend hours in discovery calls, then more hours converting rough notes into structured specification documents. Junior BAs often miss critical details, leave gaps, and produce inconsistent documentation.

**SpecForge automates this entire process.**

---

## 🚀 What It Does

SpecForge is an AI-powered agent that acts as a senior Business Analyst. It conducts a smart requirements interview, automatically identifies gaps and risks, and generates a complete professional FSD — in minutes instead of hours.

### Stage 1 — Smart Requirements Interview
The AI asks intelligent, context-aware follow-up questions (not a static form). It covers:
- Problem statement & business context
- Stakeholder identification
- Goals & success metrics
- Feature requirements
- Technical constraints & integrations

### Stage 2 — Automated Gap Analysis
After the interview, the AI analyzes the transcript and identifies:
- Missing information
- Ambiguous statements
- Contradicting requirements
- Project risks
- Unstated assumptions

### Stage 3 — Professional FSD Generation
Produces a complete, structured Functional Specification Document including:
- Executive Summary
- Project Overview (background, problem, solution)
- Stakeholder mapping
- Functional Requirements (with IDs, priorities, acceptance criteria)
- Non-Functional Requirements
- Scope definition (in/out)
- Open questions & recommended next steps
- Export as Markdown or JSON

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3, Flask, Flask-CORS |
| AI Engine | Google Gemini API (google-genai) |
| Export | Markdown, JSON |

---

## ⚡ Getting Started

### Prerequisites
- Python 3.9+
- Google Gemini API key → [Get one free at aistudio.google.com](https://aistudio.google.com)

### Installation & Run

```bash
# Clone the repo
git clone https://github.com/maleesha05/SpecForge---AI-Business-Analyst-Agent.git
cd SpecForge---AI-Business-Analyst-Agent

# Install dependencies
pip install flask flask-cors google-genai

# Set your Gemini API key
export GEMINI_API_KEY=your_api_key_here

# Start the server
python app_new.py
```

Open **http://127.0.0.1:5000** in Chrome.

---

## 📁 Project Structure

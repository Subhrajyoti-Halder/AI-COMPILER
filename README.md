# AI-COMPILER
# 🤖 AI Compiler for Software Generation

## 🚀 Overview

This project is an **AI-powered compiler system** that converts natural language into a **fully structured, validated, and executable application configuration**.

Unlike traditional prompt-based systems, this solution is designed as a **multi-stage pipeline with strict schema enforcement, validation, and automatic repair**.

---

## 🎯 Objective

Transform open-ended user instructions like:

> “Build a CRM with login, contacts, dashboard, role-based access, and payments”

into:

- UI Schema
- API Schema
- Database Schema
- Auth Rules
- Business Logic

—all **consistent, validated, and ready for execution**.

---

## 🧠 System Architecture

The system follows a **compiler-style pipeline**:
Natural Language Input
↓
Intent Extraction
↓
System Design
↓
Schema Generation
↓
Validation Engine
↓
Repair Engine
↓
Final Executable Schema


---

## ⚙️ Pipeline Stages

### 🔹 Stage 1: Intent Extraction
- Converts user input → structured JSON
- Enforces strict schema using Pydantic
- Extracts:
  - app type
  - features
  - roles
  - monetization
  - integrations

---

### 🔹 Stage 2: System Design
- Transforms intent → architecture
- Defines:
  - entities
  - flows
  - modules
  - permissions

---

### 🔹 Stage 3: Schema Generation
Generates production-ready configurations:

- UI pages
- API endpoints
- Database schema
- Authentication rules

---

### 🔹 Stage 4: Validation Engine (Core)
Performs cross-layer validation:

- UI ↔ API consistency
- API ↔ Database mapping
- Auth rule correctness

Example issue detected:
API path '/dashboard' does not map to DB table


---

### 🔹 Stage 5: Repair Engine (Advanced)
Automatically fixes issues without full regeneration.

Example:
Missing DB table → auto-created


This ensures:
- robustness
- execution readiness
- minimal manual intervention

---

## 🔐 Key Features

✅ Multi-stage compiler architecture  
✅ Strict schema enforcement (Pydantic)  
✅ Deterministic structured outputs  
✅ Cross-layer validation engine  
✅ Automatic repair system  
✅ Execution-aware design  

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI)
- Groq API (LLM inference)
- Pydantic (schema validation)

---

## ▶️ How to Run

### 1. Clone Repo :
https://github.com/Subhrajyoti-Halder/AI-COMPILER/tree/main

### 2. Install Dependencies :
pip install -r requirements.txt

### 3. Add Environment Variables :
Create .env file:
GROQ_API_KEY=your_api_key
MODEL_NAME=llama-3.3-70b-versatile

### 4. Run App :
streamlit run app.py

## 🧪 Example Input :
Build a CRM with login, contacts, dashboard,
role-based access, premium plan with payments.
Admins can see analytics.

## 📊 Example Output :
   Structured JSON across all stages
   Validation issues detected
   Auto-repair applied
   Final consistent schema

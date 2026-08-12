


# `architecture.md`

# Day 12 – HisabDo AI Financial Assistant Architecture

## 1. Overview

The HisabDo AI Financial Assistant uses a layered architecture that separates the application, backend API, AI service, financial data, and external AI model.

The purpose of this architecture is to make the chatbot easier to integrate with the HisabDo Website, Web Application, and Mobile Application.

---

# 2. System Architecture

```text
┌──────────────────────────────┐
│            User              │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Website / Web Application /  │
│ Mobile Application           │
└──────────────┬───────────────┘
               │
               │ HTTP POST /chat
               ▼
┌──────────────────────────────┐
│       FastAPI Backend        │
│                              │
│       api.py                 │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Input Validation         │
│                              │
│       models.py              │
│       Pydantic               │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       AI Service Layer       │
│                              │
│       chatbot.py             │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
┌──────────────┐  ┌────────────────┐
│ Financial    │  │ Gemini AI API  │
│ Data         │  │                │
│ JSON / DB    │  │ AI Processing  │
└──────────────┘  └───────┬────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ AI Response       │
                 │ Validation        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ JSON Response    │
                 │ to Application   │
                 └──────────────────┘

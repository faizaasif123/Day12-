# HisabDo AI Financial Assistant – Day 12

## Project Objective

The objective of this project is to make the HisabDo AI Financial Assistant more application-ready.

The chatbot allows users to ask questions about their financial information using natural language.

The Day 12 implementation includes:

- Structured input handling
- AI request processing
- Response validation
- Error handling
- FastAPI API/service layer
- Gemini AI integration

---

## AI Feature

### AI Financial Assistant / Chatbot

The selected AI feature is an AI-powered financial chatbot for HisabDo.

Users can ask questions such as:

- How much did I spend this month?
- Who owes me the most?
- How much did I spend on food?
- What are my total receivables?
- What are my total payables?

The chatbot retrieves the user's financial information and generates a natural-language response.

---

## Technology Used

- Python
- FastAPI
- Pydantic
- Google Gemini API
- Uvicorn
- JSON

### Technology Purpose

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend API and service layer |
| Pydantic | Request and response validation |
| Google Gemini API | AI response generation |
| Uvicorn | Runs the FastAPI server |
| JSON | Sample financial data |

---

## AI Model / API

The project uses the Google Gemini API for natural-language processing.

The AI receives:

- User question
- User-specific financial information
- Instructions to use only the provided information

The chatbot is instructed not to invent financial numbers.

The Gemini API key is stored in an environment variable and is not included in the source code.

---

# API

## Endpoint

```text
POST /chat


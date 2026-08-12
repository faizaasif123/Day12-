


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


Request Flow
User
 ↓
Application
 ↓
POST /chat
 ↓
FastAPI
 ↓
Validate Request
 ↓
Find User Financial Data
 ↓
Create AI Prompt
 ↓
Gemini API
 ↓
Receive AI Response
 ↓
Validate Response
 ↓
Return JSON
 ↓
Application
 ↓
User

Step-by-Step Processing
Step 1 – User Input
The user enters a natural-language financial question.
Example:
{
  "user_id": "USR001",
  "question": "How much did I spend this month?"
}

Step 2 – Application
The Website, Web Application, or Mobile Application sends the request to the backend.
POST /chat

Step 3 – FastAPI Backend
FastAPI receives the request and passes it to the Pydantic validation layer.

Step 4 – Input Validation
Pydantic validates:
•	User ID 
•	Question 
•	Required fields 
•	Minimum length 
•	Maximum length 
Invalid requests are rejected before reaching the AI service.

Step 5 – Financial Data Retrieval
The AI service retrieves the financial information associated with the supplied user ID.
Current POC:
JSON file
Future production version:
HisabDo Database

Step 6 – AI Service
The chatbot.py service creates a controlled prompt containing:
•	User financial information 
•	User question 
•	Instructions for the AI 
The service instructs the model not to invent financial values.

Step 7 – Gemini AI API
The request is sent to the Gemini AI service.
The AI processes the prompt and generates a natural-language response.

Step 8 – Response Validation
The system checks that:
•	An AI response was received. 
•	The response is not empty. 
•	The response can safely be returned to the application. 



Step 9 – API Response
FastAPI returns a structured JSON response.
Example:
{
  "user_id": "USR001",
  "question": "How much did I spend this month?",
  "answer": "Your monthly expenses are PKR 62,000.",
  "status": "success"
}

Application Integration
The chatbot can later be integrated into three HisabDo platforms.
Website
Website Chat UI
      ↓
FastAPI /chat
      ↓
AI Service
      ↓
Gemini
Web Application
Web App Chat Interface
      ↓
Backend API
      ↓
AI Service
      ↓
Gemini
Mobile Application
Mobile Chat Screen
      ↓
HTTPS API Request
      ↓
FastAPI Backend
      ↓
AI Service
      ↓
Gemini
The AI service remains centralized so all applications can use the same chatbot logic.

API Layer
The main endpoint is:
POST /chat
Request
{
  "user_id": "USR001",
  "question": "Who owes me the most?"
}
Response
{
  "user_id": "USR001",
  "question": "Who owes me the most?",
  "answer": "Ali Traders owes you PKR 45,000.",
  "status": "success"
}

Error Handling Architecture
Request
   ↓
Input Validation
   │
   ├── Invalid Input
   │       ↓
   │   Validation Error
   │
   ▼
User Lookup
   │
   ├── User Not Found
   │       ↓
   │   404 Error
   │
   ▼
AI Service
   │
   ├── API Failure
   │       ↓
   │   Controlled 500 Error
   │
   ▼
AI Response
   │
   ├── Empty Response
   │       ↓
   │   Error Handling
   │
   ▼
Validated Response
   ↓
Application

8. Data Privacy
The chatbot processes financial information, therefore privacy is an important consideration.
Current POC:
•	Uses sample financial data. 
•	Does not use real customer information. 
•	API keys are stored in environment variables. 
Production system should:
•	Authenticate users. 
•	Authorize access to financial records. 
•	Send only necessary data to the AI service. 
•	Use HTTPS. 
•	Protect database credentials. 
•	Avoid logging sensitive financial information. 
•	Implement access controls. 

9. API Cost Considerations
The chatbot depends on an external Gemini API.
Potential cost factors include:
•	Number of requests 
•	Input tokens 
•	Output tokens 
•	Selected model 
•	API usage tier 
Possible cost-control strategies:
•	Keep prompts concise. 
•	Limit response length. 
•	Avoid unnecessary AI requests. 
•	Cache suitable responses/data. 
•	Monitor API usage. 

10. Response Latency
The chatbot's response time depends partly on the external AI service.
Factors include:
•	Network speed 
•	Prompt size 
•	Model processing 
•	API load 
•	Backend processing 
Future production improvements can include:
•	Request timeouts 
•	Performance monitoring 
•	Caching 
•	Efficient prompts 
•	Background processing for long-running tasks 

11. Rate Limits
The external AI service may apply rate limits.
Possible limits include:
•	Requests per minute 
•	Requests per day 
•	Token limits 
•	Account-level usage limits 
The production application should also implement its own rate limiting to prevent excessive requests from individual users.

12. Security
Important security controls include:
API Key Security
The Gemini API key is stored in:
.env
It must never be uploaded to GitHub.
Authentication
Production users should authenticate before accessing the chatbot.
Authorization
A user should only be able to access their own financial information.
HTTPS
Production communication should use HTTPS.
Input Validation
All incoming requests should be validated before processing.
Rate Limiting
Requests should be limited to prevent abuse.
Prompt Injection Protection
User input should not be allowed to override system instructions or expose another user's financial data.

13. Hallucination and AI Error Handling
AI models can generate incorrect information.
The chatbot reduces this risk by providing the user's financial information directly to the AI and instructing it:
Use only the financial data provided.
Do not invent financial numbers.
If the required information is unavailable,
say that the information is unavailable.
For a production system, important numerical answers should also be calculated directly by backend/database logic rather than relying entirely on generated text.
Database
   ↓
Calculate total expenses
   ↓
AI explains result
This provides greater reliability for financial information.

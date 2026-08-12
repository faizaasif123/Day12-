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

Input Format
{
  "user_id": "USR001",
  "question": "How much did I spend this month?"
}
Input Fields
Field	Type	Required	Description
user_id	String	Yes	Unique user ID
question	String	Yes	User's financial question
The API validates the input before sending the request to the AI service.

Output Format
{
  "user_id": "USR001",
  "question": "How much did I spend this month?",
  "answer": "Your monthly expenses are PKR 62,000.",
  "status": "success"
}

Error Handling
The API handles the following errors.
1. Invalid User ID
If the requested user does not exist:
{
  "detail": "User ID not found."
}
The API returns HTTP 404.
2. Missing Input
If a required field is missing:
{
  "user_id": "USR001"
}
FastAPI/Pydantic returns a validation error because the question field is required.

3. Invalid Input
The API validates:
•	Required fields 
•	Minimum input length 
•	Maximum input length 
•	Input data type 
Invalid requests are rejected before reaching the AI service.

4. AI/API Failure
If the Gemini API fails because of an API, network, configuration, or service problem, the backend catches the error and returns:
{
  "detail": "Unable to process the AI request."
}
The technical error is logged on the server for debugging.

5. Empty AI Response
If the AI service returns an empty response, the system treats it as an error instead of returning an empty answer to the user.


6. Server Error
Unexpected errors are handled by the API layer and a controlled error response is returned to the user.
Internal implementation details are not exposed in the API response.

AI Request Processing
The chatbot follows these steps:
User Question
      ↓
Input Validation
      ↓
Find User Financial Data
      ↓
Create AI Prompt
      ↓
Send Request to Gemini
      ↓
Receive AI Response
      ↓
Validate Response
      ↓
Return JSON Response





Data Privacy
Financial information is sensitive.
The current project uses sample financial data for the proof-of-concept.
For production:
•	Users should be authenticated. 
•	Users should only access their own financial data. 
•	Only required financial information should be sent to the AI service. 
•	HTTPS should be used. 
•	Sensitive information should not be stored unnecessarily in logs. 
•	API keys should be stored securely. 
•	Real customer data should not be used in development/testing datasets. 
The Gemini API key is stored using an environment variable and should never be uploaded to GitHub.
API Cost Considerations
The chatbot uses an external Gemini API.
API usage may depend on:
•	Number of requests 
•	Input tokens 
•	Output tokens 
•	Selected model 
•	Account/API usage limits 
To reduce unnecessary costs:
•	Keep prompts concise. 
•	Avoid unnecessary AI requests. 
•	Limit response size where appropriate. 
•	Monitor API usage. 
•	Use caching where suitable. 

Response Latency
The chatbot depends on an external AI API, so response time can vary.
Latency may depend on:
•	Internet connection 
•	Prompt size 
•	AI model processing time 
•	API server load 
•	Backend processing 
For production, timeout handling, monitoring, caching, and prompt optimization can be implemented.
Rate Limits
The external Gemini API may have usage limits depending on the model and account/API tier.
Possible limits include:
•	Requests per minute 
•	Requests per day 
•	Token usage 
•	Account quotas 
The production application should also implement application-level rate limiting to prevent excessive requests.
Security
The following security measures are required for production:
•	Secure API-key storage 
•	User authentication 
•	User authorization 
•	HTTPS 
•	Input validation 
•	Rate limiting 
•	Secure database access 
•	Protection against prompt injection 
•	Protection of financial information 
The Gemini API key must never be hard-coded or uploaded to GitHub.
Hallucination and AI Error Handling
AI models can sometimes generate incorrect information.
To reduce hallucination, the chatbot is instructed:
Use only the financial data provided.
Do not invent financial numbers.
If the requested information is unavailable,
say that the information is unavailable.
The system also checks that the AI response is not empty.
For a production financial application, important numerical calculations should preferably be performed by backend/database logic and then explained by the AI.
Installation
Install the required Python packages:
pip install -r requirements.txt
Environment Setup
Create a .env file in the project folder:
GEMINI_API_KEY=your_gemini_api_key
Do not upload .env to GitHub.
Add this to .gitignore:
.env
__pycache__/
*.pyc
Run the API
Start the FastAPI server:
uvicorn api:app --reload
The API will run at:
http://127.0.0.1:8000
Test the API
Open the FastAPI Swagger documentation:
http://127.0.0.1:8000/docs
Select:
POST /chat
Click Try it out and enter:
{
  "user_id": "USR001",
  "question": "How much did I spend this month?"
}
Click Execute to test the chatbot.
Integration Flow
The planned integration is:
User
  ↓
Website / Web Application / Mobile Application
  ↓
Backend / FastAPI API
  ↓
Input Validation
  ↓
AI Service
  ↓
Gemini AI API
  ↓
Response Validation
  ↓
JSON Response
  ↓
Application
  ↓
User
The detailed architecture is available in architecture.md.

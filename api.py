from fastapi import FastAPI, HTTPException
from models import ChatRequest, ChatResponse
from chatbot import ask_ai


app = FastAPI(
    title="HisabDo AI Financial Assistant",
    description="Day 12 Application-Ready AI Chatbot API",
    version="3.0"
)


@app.get("/")
def home():

    return {
        "message": "HisabDo AI Financial Assistant API",
        "status": "running"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        answer = ask_ai(
            request.user_id,
            request.question
        )

        return ChatResponse(
            user_id=request.user_id,
            question=request.question,
            answer=answer,
            status="success"
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        print("API ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail="Unable to process the AI request."
        )
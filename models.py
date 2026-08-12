from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    user_id: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    question: str = Field(
        ...,
        min_length=3,
        max_length=500
    )


class ChatResponse(BaseModel):

    user_id: str
    question: str
    answer: str
    status: str
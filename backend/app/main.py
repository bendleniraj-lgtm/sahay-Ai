import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI(title="Sahay AI", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


@app.get("/")
def read_root():
    return {"message": "Welcome to Sahay AI API"}


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "sahay-ai-backend"}


@app.post("/api/chat")
def chat(req: ChatRequest):
    if not client:
        return {
            "reply": "OpenAI API key is not configured. Add OPENAI_API_KEY to your environment to enable AI responses.",
            "status": "warning",
        }

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are Sahay AI, a helpful assistive assistant. Keep responses concise, friendly, and practical.",
                },
                {"role": "user", "content": req.message},
            ],
            temperature=0.7,
            max_tokens=400,
        )

        reply = completion.choices[0].message.content.strip()
        return {"reply": reply, "status": "success"}
    except Exception as exc:  # pragma: no cover - defensive fallback
        return {
            "reply": f"The AI service is temporarily unavailable. Please try again later. Error: {str(exc)[:200]}",
            "status": "error",
        }

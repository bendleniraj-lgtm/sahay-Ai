from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


@app.get("/")
def read_root():
    return {"message": "Welcome to Sahay AI API"}


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "sahay-ai-backend"}


@app.post("/api/chat")
def chat(req: ChatRequest):
    return {
        "reply": f"Thanks for your message: {req.message}",
        "status": "success",
    }

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Question(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer_question(data: Question):
    return {
        "answer": "This is a placeholder answer from your Virtual TA.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/",
                "text": "TDS Discourse Home"
            }
        ]
    }

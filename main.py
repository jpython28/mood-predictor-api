import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Text(BaseModel):
    text: str

class Prediction(BaseModel):
    label: str
    confidence: float

class Status(BaseModel):
    status: str

app = FastAPI()

@app.post("/predict", response_model=Prediction)
def predict(text: Text):
    if len(text.text) > 500:
        raise HTTPException(413, "Text longer than 500 characters")
    if text.text == "":
        raise HTTPException(400, "Text is empty")
    label = random.choice(["positive", "negative", "neutral"])
    confidence = random.random()
    return {
        "label": label,
        "confidence": confidence,
    }

@app.get("/health", response_model=Status)
def get_health():
    return {
        "status": "ok",
    }
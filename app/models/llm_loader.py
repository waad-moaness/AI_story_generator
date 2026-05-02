import os
from dotenv import load_dotenv
from pydantic_ai.models.groq import GroqModel

load_dotenv()

_model: GroqModel | None = None

def load_model(model_name: str = "llama-3.3-70b-versatile") -> GroqModel:
    global _model
    if _model is None:
        _model = GroqModel(model_name)
    return _model
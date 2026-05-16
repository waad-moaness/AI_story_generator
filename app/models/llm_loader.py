import os
from dotenv import load_dotenv
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.models.groq import GroqModel

load_dotenv()

_gemini_model: GoogleModel | None = None
_llama_model: GroqModel | None = None

def load_primary_model(model_name: str = "gemini-3-flash-preview") -> GoogleModel:
    global _gemini_model
    if _gemini_model is None:

        _gemini_model = GoogleModel(model_name)
    return _gemini_model

def load_backup_model(model_name: str = "llama-3.3-70b-versatile") -> GroqModel:
    global _llama_model
    if _llama_model is None:
       
        _llama_model = GroqModel(model_name)
    return _llama_model
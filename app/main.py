from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from app.models.llm_loader import load_primary_model
from app.api.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading model...")
    app.state.model = load_primary_model()
    print("Model loaded.")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
from fastapi import APIRouter, Request
from app.util.prompt_format import format_prompt
from app.util.story_agent import story_agent
from app.services.story_generator import generate_story
from typing import Annotated
from pydantic import BaseModel, Field

class StoryRequest(BaseModel):
    theme: str
    goal: str
    tasks: Annotated[list[str], Field(min_length=7, max_length=7)]

router = APIRouter()

@router.get("/")
def read_root():
    return {"health_check": "OK"}

@router.post("/generate_story")
async def generate_story_endpoint(data: StoryRequest, request: Request):
    model = request.app.state.model

    prompt = format_prompt(data.theme, data.goal, data.tasks)
    agent = story_agent(model)
    story = await generate_story(agent, prompt)

    return story
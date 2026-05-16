from pydantic import BaseModel
from typing import List
from pydantic_ai import Agent
from pydantic_ai.settings import ModelSettings

class Day(BaseModel):
    day: int
    title: str
    story: str

class Section(BaseModel):
    title: str 
    story: str  

class StorySchema(BaseModel):
    intro: Section
    days: List[Day]
    outro: Section


def story_agent(model):
    agent = Agent(
        model=model,
        system_prompt="You are a creative storytelling assistant for children. Your job is to create engaging, 7-day adventure stories based on the themes and tasks provided by the user.",
        output_type=StorySchema,
        model_settings=ModelSettings(
              temperature=0.7
          ) 
    )
    return agent
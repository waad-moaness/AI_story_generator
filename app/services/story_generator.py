
async def generate_story(agent,prompt):
    result = await agent.run(prompt)
    
    data_dict = result.output.model_dump()
    return data_dict

# async def generate_story(agent,prompt):
#     result = await agent.run(prompt)
    
#     data_dict = result.output.model_dump()
#     return data_dict

import logging
from app.models.llm_loader import load_backup_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def generate_story(agent, prompt):
    try:
        logger.info("generating story with primary model (Gemini)...")
        result = await agent.run(prompt)
        
        data_dict = result.output.model_dump()
        return data_dict

    except Exception as e:
        logger.warning(f"Primary model failed : {str(e)}. Initiating Llama fallback...")
        
        try:
           
            backup_llm = load_backup_model()
            
            agent.model = backup_llm
            logger.info("Agent model successfully swapped to Llama. Retrying generation...")
            
            result = await agent.run(prompt)
            
            data_dict = result.output.model_dump()
            return data_dict
            
        except Exception as fallback_error:
            logger.error(f"Critical: Both primary and backup models failed! {str(fallback_error)}")
            raise fallback_error
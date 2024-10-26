from fastapi import APIRouter, HTTPException
from app.api.v1.schemas.request_schema import GenerateResponseRequest
from app.api.v1.schemas.response_schema import GenerateResponseOutput
from app.services.response_parser import get_parsed_response
from app.services.prompt_builder import build_prompt
from app.core.logger import logger

# Create a router for the API
router = APIRouter()

@router.post("/get_fields", response_model=GenerateResponseOutput)
async def generate_response(request: GenerateResponseRequest):
    logger.info("Received request to generate response.")
    try:
        # Build the prompt from user input
        prompt = build_prompt(request.clause)
        
        # Call the LLM client to get a response
        parsed_response = get_parsed_response(prompt)
        logger.info("Response successfully parsed")

        return GenerateResponseOutput(response=parsed_response)

    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail=str(e))

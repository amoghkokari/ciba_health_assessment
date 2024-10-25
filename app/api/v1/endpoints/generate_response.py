from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.llm_client import LLMClient
from app.services.prompt_builder import build_prompt
from app.services.response_parser import parse_response

# Create a router for the API
router = APIRouter()

# Define the request model
class GenerateResponseRequest(BaseModel):
    user_input: str = Field(..., example="What are the insurance requirements for health coverage?")

# Define the response model
class GenerateResponseOutput(BaseModel):
    response: str

@router.post("/get_fields", response_model=GenerateResponseOutput)
async def generate_response(request: GenerateResponseRequest):
    try:
        # Build the prompt from user input
        prompt = build_prompt(request.user_input)
        
        # Call the LLM client to get a response
        llm_client = LLMClient()
        llm_response = await llm_client.get_response(prompt)
        
        # Parse the response from the LLM
        parsed_response = parse_response(llm_response)

        return GenerateResponseOutput(response=parsed_response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from fastapi import APIRouter, HTTPException
from app.api.v1.schemas.request_schema import GenerateResponseRequest
from app.api.v1.schemas.response_schema import GenerateResponseOutput
from app.services.llm_client import GeminiClient
from app.services.prompt_builder import build_prompt
from app.services.response_parser import parse_response

# Create a router for the API
router = APIRouter()

@router.post("/get_fields", response_model=GenerateResponseOutput)
async def generate_response(request: GenerateResponseRequest):
    try:
        # Build the prompt from user input
        prompt = build_prompt(request.user_input)

        print(prompt)
        
        # Call the LLM client to get a response
        llm_client = GeminiClient
        llm_response = llm_client.generate_content(prompt)
        
        # Parse the response from the LLM
        parsed_response = parse_response(llm_response)

        return GenerateResponseOutput(response=parsed_response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

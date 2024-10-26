import azure.functions as func
from app.services.response_parser import get_parsed_response
from app.services.prompt_builder import build_prompt
from app.core.logger import logger
import json

# Azure Function app instance
function_app = func.FunctionApp()

@function_app.route(route="health", methods=["GET"])
async def health_check(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Healthy", status_code=200)

@function_app.route(route="get_fields", methods=["POST"])
async def generate_response(req: func.HttpRequest) -> func.HttpResponse:
    logger.info("Received request to generate response.")
    try:
        # Build the prompt from user input
        request_body = req.get_json()
        prompt = build_prompt(request_body['clause'])
        
        # Call the LLM client to get a response
        parsed_response = get_parsed_response(prompt)
        logger.info("Response successfully parsed")

        return func.HttpResponse(json.dumps(parsed_response), status_code=200, mimetype="application/json")
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise func.HTTPException(status_code=500, detail=str(e))

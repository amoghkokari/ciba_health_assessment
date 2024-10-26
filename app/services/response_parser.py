from app.services.llm_client import GeminiClient
from json import loads as jLoads, dumps as jDumps
from re import search, DOTALL

def parse_response(response) -> str:
    """
    Parses the LLM response to extract the required information.

    Args:
        response : The response from the LLM.

    Returns:
        str: The extracted information from the response.
    """
    # Adjust according to the structure of the LLM response

    if response.text:
        try:
            json_text = search(r'\{.*\}', response.text, DOTALL).group()
            formatted_json = jLoads(json_text)
            return formatted_json
        except Exception as e:
            raise e
           
    return "Invalid response format"

def get_parsed_response(prompt):
    llm_client = GeminiClient()
    llm_response = llm_client.generate_content(prompt)

    # Parse the response from the LLM
    return parse_response(llm_response)
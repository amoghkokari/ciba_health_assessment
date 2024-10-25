from pydantic import BaseModel

# Define the response model
class GenerateResponseOutput(BaseModel):
    response: str

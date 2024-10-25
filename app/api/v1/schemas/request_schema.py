from pydantic import BaseModel, Field

# Define the request model
class GenerateResponseRequest(BaseModel):
    clause: str = Field(..., example="What are the insurance requirements for health coverage?")

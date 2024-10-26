import pytest
from app.services.prompt_builder import build_prompt, validate_prompt
from app.services.prompt_templates import get_contruction_insurance_agent

def test_build_prompt():
    user_input = "What are the insurance requirements for health coverage?"
    prompt = build_prompt(user_input)
    assert get_contruction_insurance_agent() in prompt

def test_validate_prompt():
    valid_prompt = "Extract the insurance requirements from the following clause: Test"
    invalid_prompt = ""
    
    assert validate_prompt(valid_prompt) is True
    assert validate_prompt(invalid_prompt) is False

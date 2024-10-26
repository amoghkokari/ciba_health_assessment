import pytest
from app.services.response_parser import parse_response

class MockResponse:
    def __init__(self, text):
        self.text = text

def test_parse_response_valid():
    response = MockResponse('{"data": {"extracted_info": "Sample insurance requirements"}}')
    extracted_info = parse_response(response)
    
    assert extracted_info == "Sample insurance requirements"

def test_parse_response_invalid():
    response = {"unexpected_key": "Some data"}
    extracted_info = parse_response(response)
    
    assert extracted_info == "Invalid response format"

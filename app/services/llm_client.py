import google.generativeai as genai
from ciba_health_assessment.app.core.config import gamini_llm_api_key

def GeminiClient():
    llm_api_key = gamini_llm_api_key if gamini_llm_api_key else ""
    genai.configure(api_key=llm_api_key)
    model = genai.GenerativeModel(model_name = "gemini-pro")
    
    return model
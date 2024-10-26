# from os import environ
from app.core.config import config
import google.generativeai as genai

def GeminiClient():
    llm_api_key = config.llm_api_key
    genai.configure(api_key=llm_api_key)
    gen_config = genai.GenerationConfig(temperature=0.0, top_p=1, top_k=1)
    model = genai.GenerativeModel(model_name = "gemini-1.0-pro", generation_config = gen_config)
    
    return model

    # candidate_count: int | None = None
    # stop_sequences: Iterable[str] | None = None
    # max_output_tokens: int | None = None
    # temperature: float | None = None
    # top_p: float | None = None
    # top_k: int | None = None
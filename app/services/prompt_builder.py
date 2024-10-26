from prompt_templates import get_contruction_insurance_agent, get_construction_industry_specifics, get_insurance_mapping_fields, get_contruction_insurance_examples

def build_prompt(user_input: str) -> str:
    """
    Constructs a prompt for the LLM based on user input.

    Args:
        user_input (str): The input provided by the user.

    Returns:
        str: The formatted prompt for the LLM.
    """
    # Here you can customize the prompt format as needed

    task = """Your task is to understand construction industry based on provided CONTEXT, 
    Extract five MAPPING FIELDS from the INPUT TEXT based on CONTEXT AND BACKGROUND 
    Return answer as JSON object, the JSON output should include fields for the four specified insurance types, with up to four fields each:
        General Liability Insurance
        Automobile Liability Insurance
        Workers' Compensation Insurance
        Professional Liability Insurance
    Include a separate section for any "additional insured" entities, containing only the entity name and type of coverage for only General Liability
    map fields based on MAPPING FIELDS. Refer to EXAMPLE
    Do not infer any data based on previous training, strictly use only INPUT TEXT as input."""

    prompt = get_contruction_insurance_agent+"/n/nCONTEXT = "+get_construction_industry_specifics+"/n/nMAPPING FIELDS = "+get_insurance_mapping_fields+"/n/nINPUT TEXT = "+user_input+"/n/n"+task

    return prompt

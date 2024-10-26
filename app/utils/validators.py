from typing import Any

def validate_clause_length(clause: str, min_length: int = 10) -> bool:
    """
    Validates that the clause is not too short, ensuring it has a minimum length.

    Args:
        clause (str): The clause to validate.
        min_length (int): Minimum acceptable length for the clause.

    Returns:
        bool: True if clause is valid, False otherwise.
    """
    return len(clause.strip()) >= min_length

def validate_non_empty_input(input_value: Any) -> bool:
    """
    Checks if the input is not empty.

    Args:
        input_value (Any): The value to validate.

    Returns:
        bool: True if the input is not empty, False otherwise.
    """
    return bool(input_value and str(input_value).strip())

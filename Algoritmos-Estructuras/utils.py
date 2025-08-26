# utils.py
import re

def extract_numbers(input_string):
    if not isinstance(input_string, str):
        return []  # o lanza una excepción más clara

    pattern = r"-?\d+\.?\d*"
    matches = re.findall(pattern, input_string)
    numbers = [float(num) if '.' in num else int(num) for num in matches]
    return numbers

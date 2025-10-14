import re

def validate_hex_string(hex_string):
    hex_regular_expression = r"#[0-9a-fA-F]{6}"
    return re.fullmatch(hex_regular_expression, hex_string)

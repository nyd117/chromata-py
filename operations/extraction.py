import re

HEX_PATTERN: str = "#[0-9a-fA-F]{6}"


def extract(text_input: str) -> list:
    matches = re.findall(f"({HEX_PATTERN})", text_input)

    if matches:
        return matches
    else:
        return []


def is_valid_hex_color(color: str) -> bool:
    return re.match(f"^{HEX_PATTERN}$", color) is not None

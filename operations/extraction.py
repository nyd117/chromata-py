import re

from operations.color_conversions import Color
from runtime_constants import HEX_PATTERN


def extract(text_input: str) -> list:
    matches = re.findall(f"({HEX_PATTERN})", text_input)

    if matches:
        return list(map(lambda hex_color: Color(hex_color), matches))
    else:
        return []

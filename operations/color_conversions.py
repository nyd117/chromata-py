from typing import Tuple
from operations.extraction import is_valid_hex_color


def hex_to_rgb(color: str) -> Tuple[int, int, int]:
    return tuple(bytes.fromhex(color.strip("#")))


def rgb_to_hex(color: Tuple[int, int, int]) -> str:
    hex_color = "#%02x%02x%02x" % tuple(color)
    return hex_color


def invert_hex(color: str) -> str:
    inv_r: int = 0
    inv_g: int = 0
    inv_b: int = 0
    if is_valid_hex_color(color):
        color_raw: bytes = bytes.fromhex(color.strip("#"))
        r: int = color_raw[0]
        g: int = color_raw[1]
        b: int = color_raw[2]
        inv_r = 255 - r
        inv_g = 255 - g
        inv_b = 255 - b

    return rgb_to_hex((inv_r, inv_g, inv_b))

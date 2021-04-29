import colorsys
import math
import re
from typing import Tuple, cast

from runtime_constants import HEX_PATTERN


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


def is_valid_hex_color(color: str) -> bool:
    return re.match(f"^{HEX_PATTERN}$", color) is not None


class Color:
    def __init__(self, hex_value):
        self.hex_color = hex_value

    def __str__(self):
        return self.hex_color

    def __eq__(self, other):
        return self.hex_color == other.hex_color

    def __hash__(self):
        return hash(('hex_color', self.hex_color))

    @property
    def rgb(self):
        return hex_to_rgb(self.hex_color)

    @property
    def r(self):
        return self.rgb[0]

    @property
    def g(self):
        return self.rgb[1]

    @property
    def b(self):
        return self.rgb[2]

    @property
    def rgb_string(self):
        return ','.join(str(s) for s in self.rgb)


def rgb_to_yiq(color: Color):
    col = colorsys.rgb_to_yiq(*hex_to_rgb(color.hex_color))
    col = tuple(map(int, col))
    return rgb_to_hex(cast(Tuple[int, int, int], col))


def step_lum_hsv(color: Color, repetitions=1):
    lum = get_perceived_brightness(color)
    h, s, v = colorsys.rgb_to_hsv(color.r, color.g, color.b)
    h2 = int(h * repetitions)
    v2 = int(v * repetitions)

    return h2, lum, v2


def step_inv_lum_hsv(color: Color, repetitions=1):
    lum = get_perceived_brightness(color)
    h, s, v = colorsys.rgb_to_hsv(color.r, color.g, color.b)
    h2 = int(h * repetitions)
    v2 = int(v * repetitions)
    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum
    return h2, lum, v2


def get_perceived_brightness(color: Color):
    return math.sqrt(.241 * color.r * color.r + .691 * color.g * color.g + .068 * color.b * color.b)

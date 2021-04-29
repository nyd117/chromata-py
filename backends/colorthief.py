import sys
from typing import List

import operations.color_conversions
from backends.backend import Backend
from operations.color_conversions import Color

try:
    from colorthief import ColorThief

except ImportError:
    sys.exit(1)


class ColorThiefBackend(Backend):
    def get_colors(self, image, color_number=8) -> List[Color]:
        raw_colors = ColorThief(image).get_palette(color_number+1)

        return [Color(operations.color_conversions
                .rgb_to_hex(color))
                for color in raw_colors]

import sys
from typing import List

import operations.color_conversions
from backends.backend import Backend
from operations.color_conversions import Color

try:
    from colorz import colorz

except ImportError:
    sys.exit(1)


class ColorZ(Backend):
    def get_colors(self, image, color_number=8) -> List[Color]:
        raw_colors = colorz(image, n=color_number, bold_add=0)

        return [Color(operations.color_conversions
                .rgb_to_hex(color[0]))
                for color in raw_colors]

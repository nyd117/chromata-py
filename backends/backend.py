from abc import abstractmethod
from typing import List

from operations.color_conversions import Color


class Backend:
    @abstractmethod
    def get_colors(self, image, color_number=8) -> List[Color]:
        """
        This abstract method should return a List[str]
        :rtype: List[str]
        """
        pass

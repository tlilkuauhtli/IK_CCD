"""
Draw scene elements
"""

# Standard library
import logging
from dataclasses import dataclass

# Third-party
import pygame as pg


logger = logging.getLogger("Scene")

@dataclass
class Scene:
    """
    Scene class
    """

    width: int
    height: int
    screen: pg.surface.Surface

    def draw_grid(self, color: pg.Color) -> None:
        """
        Draw grid

        Parameters
        ----------
        color : pg.Color
            Pygame color object, color name or tuple (RGB[A])
        """

        for i in range(0, self.height + 1, 20):
            pg.draw.line(
                self.screen, color, (0, i), (self.width, i))

        for i in range(0, self.width + 1, 20):
            pg.draw.line(
                self.screen, color, (i, 0), (i, self.height))

    def draw_main_axes(self, color: pg.Color, centre: pg.math.Vector2) -> None:
        """
        Draw x and y axes

        Parameters
        ----------
        color : pg.Color
            Pygame color object, color name or tuple (RGB[A])
        centre : pg.math.Vector2
            Point vector
        """

        pg.draw.line(
            self.screen, color, (self.screen.get_width() / 2, 0),
            (self.screen.get_width() / 2, self.screen.get_height()))
        pg.draw.line(
            self.screen, (127, 127, 0, 1), (0, self.screen.get_height() / 2),
            (self.screen.get_width(), self.screen.get_height() / 2))

        pg.draw.circle(self.screen, "yellow", centre, 5)

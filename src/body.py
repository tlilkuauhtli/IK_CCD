"""
Body
"""

# Standard library
# from enum import Enum
from dataclasses import dataclass, field

# Third-party
import pygame as pg


@dataclass
class Body:
    """
    Body class
    """

    screen: pg.surface.Surface
    centre: pg.math.Vector2
    link_list: list = field(default_factory=list)

    def __post_init__(self):
        """
        Set up initial list
        """

        self.link_list.append(self.centre)
        self.link_list.append(
            pg.math.Vector2(self.centre.x + 50, self.centre.y - 110))
        self.link_list.append(
            pg.math.Vector2(self.centre.x + 10, self.centre.y - 150))
        self.link_list.append(
            pg.math.Vector2(self.centre.x - 20, self.centre.y - 180))

    def draw_body(self):
        """
        Draw body links
        """

        pg.draw.lines(self.screen, "red", False, self.link_list)
        for coord in self.link_list:
            pg.draw.circle(self.screen, "orange", coord, 5)

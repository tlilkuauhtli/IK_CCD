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
        self.link_list.append((self.centre.x + 50, self.centre.y - 110))
        self.link_list.append((self.centre.x + 10, self.centre.y - 150))
        self.link_list.append((self.centre.x - 20, self.centre.y - 180))

    def draw_body(self):
        """
        Draw body links
        """

        first: tuple = None
        for index, coord in enumerate(self.link_list):
            if first is None:
                first = coord
                continue

            pg.draw.circle(self.screen, "orange", first, 5)
            pg.draw.line(self.screen, "red", first, coord)

            if index == len(self.link_list) - 1:
                pg.draw.circle(self.screen, "orange", coord, 5)

            first = coord


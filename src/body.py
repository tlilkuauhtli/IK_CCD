"""
Body
"""

# Standard library
from dataclasses import dataclass

# Third-party
import pygame as pg


@dataclass
class Body:
    """
    Body class
    """

    screen: pg.surface.Surface
    centre: pg.math.Vector2
    link_list: list = []

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

        for link in self.link_list:
            pg.draw.line(
                self.screen, "red",
                (self.screen.get_width() / 2, self.screen.get_height() / 2),
                (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 - 110))

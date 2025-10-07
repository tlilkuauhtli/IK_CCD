"""
2D Space
"""

# Standard library
import math
from dataclasses import dataclass

# Third-party
import pygame as pg


@dataclass
class Space:
    """
    Class
    """

    @staticmethod
    def angle_between_vectors(u: pg.Vector2, v: pg.Vector2) -> float:
        """
        Angle between vectors

        """

        angle = 0

        u_norm_x_v_norm = u.dot(v) / (u.length() * v.length())

        if u_norm_x_v_norm < 1:
            angle = math.acos(u_norm_x_v_norm) * (180 / math.pi)
        else:
            angle = float(0)

        return angle

    @staticmethod
    def cross_product(u: pg.Vector2, v: pg.Vector2) -> float:
        """
        Cross product
        u x v = det(u v) = (u_x * v_y) - (u_y * v_x)
        """

        # u.cross(v)
        result = (u.x * v.y) - (u.y * v.x)

        return result

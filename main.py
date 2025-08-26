"""
Main structure to control program
"""

# Standard library
import logging

# Third-party
import pygame as pg
from pygame.locals import *

# Local
from src.scene import Scene
from src.body import Body

logging.basicConfig(format="ik_ccd :: %(asctime)s :: %(message)s")
logger = logging.getLogger("Main")
logger.setLevel(logging.DEBUG)


HEIGHT = 800
WIDTH = 800

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Inverse Kinematics - Cyclic Coordinate Descent")
clock = pg.time.Clock()
running = True
delta_time = 0

# Create background
background = pg.Surface(screen.get_size())
background = background.convert()
# Background color
background.fill((0, 0, 0))
centre = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

logger.info(
    "Centre: %s - Type: %s - Type: %s, dir: %s",
    centre, type(centre), type(centre[0]), dir(centre))
scene = Scene(width=WIDTH, height=HEIGHT, screen=screen)
body = Body(screen, centre)

if not pg.font:
    logger.warning("Fonts disabled.")
else:
    font = pg.font.Font(None, 20)
    # Text color
    text = font.render("Body data:", True, (255, 255, 255))
    text_pos = text.get_rect(x=20, y=20)
    background.blit(text, text_pos)


# Display background
screen.blit(background, (0, 0))
pg.display.flip()


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            logger.info("Event: %s, Type: %s", event, event.type)
        # elif event.type == MOUSEWHEEL:
        #     logger.info("Event: %s", event)


    # logger.info("Mouse pos: %s", pg.mouse.get_pos())
    # logger.info("Pressed: %s", pg.mouse.get_pressed())

    # Clear screen
    screen.fill("black")

    # More instructions here

    screen.blit(background, (0, 0))

    scene.draw_grid(color=(60, 60, 0, 0.5))
    scene.draw_main_axes(color=(127, 127, 0, 1), centre=centre)

    body.draw_body()

    # Flip the display things on screen
    pg.display.flip()

    # Set FPS=60s
    # Delta time in seconds since last frame
    delta_time = clock.tick(60) / 1000
    # logger.info("Delta time: %s", delta_time)

pg.quit()

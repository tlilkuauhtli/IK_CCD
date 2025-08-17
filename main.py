"""
Main structure to control program
"""

# Third-party
import pygame as pg

pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Inverse Kinematics - Cyclic Coordinate Descent")
clock = pg.time.Clock()
running = True
delta_time = 0

# Create background
background = pg.Surface(screen.get_size())
background = background.convert()
# Background color
background.fill((0, 0, 0))

if not pg.font:
    print("Warning, fonts disabled.")
else:
    font = pg.font.Font(None, 25)
    # Text color
    text = font.render("Body data:", True, (255, 255, 255))
    text_pos = text.get_rect(x=10, y=10)
    background.blit(text, text_pos)


# Display background
screen.blit(background, (0, 0))
pg.display.flip()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Clear screen
    screen.fill("black")

    # More instructions here
    # pg.draw

    screen.blit(background, (0, 0))
    pg.display.flip()

    # Set FPS=60
    # Delta time in seconds since last frame
    delta_time = clock.tick(60) / 1000

pg.quit()

"""
Main structure to control program
"""

# Third-party
import pygame as pg

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

centre = pg.Vector2(screen.get_width()/2, screen.get_height()/2)

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


# def draw_grid():
#     """
#     Draw grid
#     """

#     for i in range(HEIGHT + 1):


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Clear screen
    screen.fill("black")

    # More instructions here
    # pg.draw

    screen.blit(background, (0, 0))
    pg.draw.circle(screen, "yellow", centre, 5)

    for i in range(0, HEIGHT + 1, 20):
        pg.draw.line(screen, (60, 60, 0, 0.5), (0, i), (WIDTH, i))

    for i in range(0, WIDTH + 1, 20):
        pg.draw.line(screen, (60, 60, 0, 0.5), (i, 0), (i, HEIGHT))

    pg.draw.line(
        screen, (127, 127, 0, 1), (screen.get_width()/2, 0),
        (screen.get_width()/2, screen.get_height()))
    pg.draw.line(
        screen, (127, 127, 0, 1), (0, screen.get_height()/2),
        (screen.get_width(), screen.get_height()/2))

    # Flip the display things on screen
    pg.display.flip()

    # Set FPS=60
    # Delta time in seconds since last frame
    delta_time = clock.tick(60) / 1000

pg.quit()

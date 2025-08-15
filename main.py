"""
Main structure to control program
"""

# Third-party
import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill("black")

    # More instructions here

    pygame.display.flip()

    # Set FPS=60
    clock.tick(60)

pygame.quit()

import pygame
import pygame.time

pygame.init()

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
running = True

# -- initialize other global variables here --

while running:
    # fill window with a background color
    # screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -- put the rest of your code here --

    pygame.display.flip()
    clock.tick(60)

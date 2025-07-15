import pygame
import pygame.time

pygame.init()

WIDTH, HEIGHT = 400, 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# -- initialize other global variables here --

while running:
    # fill window with a background color (you usually want to do this)
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -- put the rest of your code here --

    font = pygame.font.SysFont("Arial", 36)
    text = font.render("Hello, Pygame!", True, (255, 255, 255))
    screen.blit(text, (100, 100))

    pygame.display.flip()
    clock.tick(60)

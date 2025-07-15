import pygame
import pygame.time

pygame.init()

WIDTH, HEIGHT = 400, 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# -- initialize other global variables here --
last_tick = pygame.time.get_ticks()

while running:
    # fill window with a background color (you usually want to do this)
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -- put the rest of your code here --

    current_tick = pygame.time.get_ticks()
    if current_tick - last_tick >= 1000:  # 1000 ms = 1 second
        print("One second has passed")
        last_tick = current_tick

    pygame.display.flip()
    clock.tick(60)

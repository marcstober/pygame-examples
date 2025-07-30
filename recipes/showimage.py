import pygame

pygame.init()

WIDTH, HEIGHT = 400, 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# -- setup code goes here --

image = pygame.image.load("chrysler-building.jpg")  # Load your image here

running = True
while running:
    # fill window with a background color (you usually want to do this)
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -- the rest of your code goes here --
    screen.blit(image, (0, 0))  # Draw the image at (0, 0)

    pygame.display.flip()
    clock.tick(60)

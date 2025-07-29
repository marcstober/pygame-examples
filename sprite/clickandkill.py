"""
This script demonstrates how to detect and remove sprites by clicking on them in a Pygame window.
A probe sprite is created at the mouse position to check for collisions with existing sprites.
"""

import pygame
import pygame.time

from rectsprite import RectSprite


class PointSprite(pygame.sprite.Sprite):
    def __init__(self, pos, *groups) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect(topleft=pos)


pygame.init()

WIDTH, HEIGHT = 400, 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# -- initialize other global variables here --
all_sprites = pygame.sprite.Group()
color_sprite = RectSprite.create((255, 0, 0), (100, 100, 32, 50), all_sprites)

while running:
    # fill window with a background color (you usually want to do this)
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Create a 1x1 probe sprite at the mouse position
            point = PointSprite(event.pos)

            # Check for collisions
            # Use dokill=True to remove the sprites that are clicked
            clicked = pygame.sprite.spritecollide(point, all_sprites, True)
            # Alternate way to remove clicked sprites:
            # for s in clicked:
            #     s.kill()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

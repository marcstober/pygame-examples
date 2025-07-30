import random
from pathlib import Path

import pygame
import pygame.time

from sprite.imagesprite import ImageSprite
from sprite.circlesprite import CircleSprite


# define some functions to use later


def get_random_color():
    """Return a random RGB color tuple."""
    return tuple(random.randint(0, 255) for _ in range(3))


def randomly_position_sprites():
    planet.rect.topleft = (
        random.randint(0, WIDTH - planet.rect.width),
        random.randint(0, HEIGHT - planet.rect.height),
    )
    rocket.rect.topleft = (
        random.randint(0, WIDTH - rocket.rect.width),
        random.randint(0, HEIGHT - rocket.rect.height),
    )


# setup

pygame.init()
pygame.display.set_caption("Rocket Lander")

WIDTH, HEIGHT = 400, 300

font = pygame.font.SysFont("Verdana", 12)
big_font = pygame.font.SysFont("Verdana", 24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background_color = "black"
is_colliding = False
game_over = False

# create sprites

all_sprites = pygame.sprite.Group()

planet = CircleSprite.create(get_random_color(), (0, 0), 60, all_sprites)
filename = Path("sprite") / "vecteezy_pixel-rocket-ship-illustration_49496512.png"
rocket = ImageSprite.from_filename(filename, all_sprites, scale_to_size=(90, 90))

randomly_position_sprites()

running = True
while running:

    # handle events, especially quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # press any key to restart if game is over
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if game_over:
                print("Restarting")
                planet.color = get_random_color()
                randomly_position_sprites()
                is_colliding = False
                game_over = False

    if not game_over:  # play mode
        # check which keys are being pressed and move rocket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rocket.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            rocket.rect.x += 1
        if keys[pygame.K_UP]:
            rocket.rect.y -= 1
        if keys[pygame.K_DOWN]:
            rocket.rect.y += 1

        # make Mr. Rectangle wrap around when he goes off the screen
        if rocket.rect.right < 0:
            rocket.rect.left = WIDTH - 1
        elif rocket.rect.left > WIDTH:
            rocket.rect.right = 1
        if rocket.rect.bottom < 0:
            rocket.rect.top = HEIGHT - 1
        elif rocket.rect.top > HEIGHT:
            rocket.rect.bottom = 1

        if pygame.sprite.spritecollideany(
            rocket, pygame.sprite.Group(planet), pygame.sprite.collide_mask
        ):
            if not is_colliding:
                print("colliding", is_colliding)
                game_over = True
                is_colliding = True
        else:
            is_colliding = False

    # fill window with a background color
    screen.fill(background_color)

    # update and draw the sprites
    all_sprites.update()
    all_sprites.draw(screen)

    if game_over:
        text_color = (  # blink text
            (255, 0, 0) if pygame.time.get_ticks() % 1000 > 500 else (0, 255, 255)
        )
        game_over_text = big_font.render("LANDED", True, text_color)
        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                HEIGHT // 2 - game_over_text.get_height() // 2,
            ),
        )

        # font = pygame.font.SysFont("Verdana", 12)
        restart_text = font.render("press 's' to restart", True, (255, 255, 255))
        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                HEIGHT // 2 + game_over_text.get_height() // 2 + 10,
            ),
        )

    # stuff we need to do at the end of each loop iteration
    pygame.display.flip()
    clock.tick(60)

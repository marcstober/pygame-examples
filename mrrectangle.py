import random
from pathlib import Path
from tkinter.tix import MAX

import pygame
import pygame.time

from sprite.colorsprite import ColorSprite
from sprite.imagesprite import ImageSprite

# define some functions to use later


def get_random_color():
    """Return a random RGB color tuple."""
    return tuple(random.randint(0, 255) for _ in range(3))


def randomly_position_sprites():
    color_sprite.rect.topleft = (
        random.randint(0, WIDTH - color_sprite.rect.width),
        random.randint(0, HEIGHT - color_sprite.rect.height),
    )
    image_sprite.rect.topleft = (
        random.randint(0, WIDTH - image_sprite.rect.width),
        random.randint(0, HEIGHT - image_sprite.rect.height),
    )


# setup

pygame.init()
pygame.display.set_caption("Mr. Rectangle")

WIDTH, HEIGHT = 400, 300

font = pygame.font.SysFont("Verdana", 12)
big_font = pygame.font.SysFont("Verdana", 24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

MAX_SECONDS = 60
seconds_left = MAX_SECONDS  # 60
start_tick = pygame.time.get_ticks()

background_color = (0, 255, 255)
is_colliding = False
score = 0


# create sprites

all_sprites = pygame.sprite.Group()

color_sprite = ColorSprite(get_random_color(), all_sprites)
image_path = Path("sprite") / "guy.png"
image_sprite = ImageSprite(image_path, all_sprites)

randomly_position_sprites()


while running:

    # handle events, especially quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # press any key to restart if  game is over
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if seconds_left <= 0:
                print("Restarting")
                seconds_left = MAX_SECONDS  # 60
                start_tick = pygame.time.get_ticks()

    if seconds_left > 0:  # play mode (not game over)
        # check which keys are being pressed and move Mr. Rectangle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image_sprite.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            image_sprite.rect.x += 1
        if keys[pygame.K_UP]:
            image_sprite.rect.y -= 1
        if keys[pygame.K_DOWN]:
            image_sprite.rect.y += 1

        # make Mr. Rectangle wrap around when he goes off the screen
        if image_sprite.rect.right < 0:
            image_sprite.rect.left = WIDTH - 1
        elif image_sprite.rect.left > WIDTH:
            image_sprite.rect.right = 1
        if image_sprite.rect.bottom < 0:
            image_sprite.rect.top = HEIGHT - 1
        elif image_sprite.rect.top > HEIGHT:
            image_sprite.rect.bottom = 1

        # change color when sprites collide
        if pygame.sprite.collide_rect(color_sprite, image_sprite):
            if not is_colliding:
                color_sprite.set_color(get_random_color())
                background_color = get_random_color()
                randomly_position_sprites()
                score += 1
                is_colliding = True
        else:
            is_colliding = False

    # fill window with a background color
    screen.fill(background_color)

    # update and draw the sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # show score
    # font = pygame.font.SysFont("Verdana", 12)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # update timer
    # MAX_SECONDS = 60
    seconds_left = max(0, MAX_SECONDS - (pygame.time.get_ticks() - start_tick) // 1000)
    minutes = seconds_left // 60
    seconds = seconds_left % 60
    timer_text = font.render(f"Time: {minutes}:{seconds:02d}", True, (0, 0, 0))
    screen.blit(timer_text, (10, HEIGHT - timer_text.get_height() - 10))

    if seconds_left <= 0:  # GAME OVER mode
        # big_font = pygame.font.SysFont("Verdana", 36)
        game_over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                HEIGHT // 2 - game_over_text.get_height() // 2,
            ),
        )

        # font = pygame.font.SysFont("Verdana", 12)
        restart_text = font.render("press 's' to restart", True, (0, 0, 0))
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

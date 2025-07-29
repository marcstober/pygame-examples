import pygame
from circlesprite import CircleSprite
from rectsprite import RectSprite

pygame.init()

WIDTH, HEIGHT = 400, 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Use WASD to move the rectangle")

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

YELLOW = (204, 204, 0)

rect = RectSprite.create((0, 192, 0), (50, 50, 40, 70), all_sprites)
circle = CircleSprite.create(
    YELLOW, (WIDTH // 2, HEIGHT // 2), 80, obstacles, all_sprites
)


def collide_rect_circle(rect_sprite, circle_sprite) -> bool:
    closest_x = max(
        rect_sprite.rect.left, min(circle_sprite.rect.centerx, rect_sprite.rect.right)
    )
    closest_y = max(
        rect_sprite.rect.top, min(circle_sprite.rect.centery, rect_sprite.rect.bottom)
    )
    # Calculate the distance from the circle center to this point
    dx = circle_sprite.rect.centerx - closest_x
    dy = circle_sprite.rect.centery - closest_y
    return dx * dx + dy * dy <= circle_sprite.radius * circle_sprite.radius


running = True
while running:
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rect.rect.x -= 1
    if keys[pygame.K_d]:
        rect.rect.x += 1
    if keys[pygame.K_w]:
        rect.rect.y -= 1
    if keys[pygame.K_s]:
        rect.rect.y += 1

    # We could consolidate the following two loops into one loop,
    # but I wanted to give an example of the spritecollide function.

    for obstacle in obstacles:
        obstacle.color = YELLOW

    # Note that there is a built-in collide_circle function,
    # but it does not work accurately with a non-square rect.
    # Try changing it and see.
    for obstacle in pygame.sprite.spritecollide(
        rect, obstacles, False, collide_rect_circle
    ):
        obstacle.color = (204, 0, 0)

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

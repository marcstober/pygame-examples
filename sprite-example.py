import pygame
import pygame.time

SPRITE_SIZE = 70

class Character(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.image.get_rect()
        pygame.draw.circle(
            self.image, (192, 192, 192), self.rect.center, self.image.get_height() / 2
        )
        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)

pygame.init()

win_size = 400, 300
win = pygame.display.set_mode(win_size)

character1 = Character()
obstacle1 = Character()
obstacle1.rect.topleft = 100, 100
group1 = pygame.sprite.Group([character1, obstacle1])
obstacle_group = pygame.sprite.Group([obstacle1])

clock = pygame.time.Clock()
pygame.key.set_repeat(50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character1.rect.left -= 1    
            elif event.key == pygame.K_RIGHT:
                character1.rect.left += 1    
            elif event.key == pygame.K_UP:
                character1.rect.top -= 1    
            elif event.key == pygame.K_DOWN:
                character1.rect.top += 1    

    color = 0, 50, 0
    if pygame.sprite.spritecollide(character1, obstacle_group, False, pygame.sprite.collide_mask):
        color = 100, 0, 0

    win.fill(color)
    group1.update()
    group1.draw(win)
    pygame.display.flip()
    clock.tick(60)

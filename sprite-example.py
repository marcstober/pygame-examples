import pygame
import pygame.time


class MySprite(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((20, 30))
        self.image.fill("lime")
        self.rect = self.image.get_rect()

    def update(self):
        if self.rect.left > 450:
            self.image.fill("red")
        else:
            self.image.fill("lime")


pygame.init()

screen = pygame.display.set_mode((600, 400))

sprite1 = MySprite()
sprite1.rect.center = (300, 200)
group1 = pygame.sprite.Group([sprite1])

clock = pygame.time.Clock()
velocity = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite1.rect.left -= velocity
            elif event.key == pygame.K_RIGHT:
                sprite1.rect.left += velocity
            elif event.key == pygame.K_UP:
                sprite1.rect.top -= velocity
            elif event.key == pygame.K_DOWN:
                sprite1.rect.top += velocity

    screen.fill("dimgray")
    group1.update()
    group1.draw(screen)
    pygame.display.flip()
    clock.tick(60)

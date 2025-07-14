import pygame


class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, *groups) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((32, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_color(self, color):
        self.image.fill(color)

    # def update(self, *args, **kwargs):
    # You can implement logic here to update the sprite each frame

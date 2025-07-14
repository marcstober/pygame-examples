import pygame


class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, *groups) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

    # def update(self, *args, **kwargs):
    # You can implement logic here to update the sprite each frame

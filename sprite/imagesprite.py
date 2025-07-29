import pygame


class ImageSprite(pygame.sprite.Sprite):
    rect: pygame.Rect
    image: pygame.Surface

    @classmethod
    def from_filename(cls, filename, *groups):
        # This is done as a classmethod, not in the constructor,
        # to keep type checkers happy since they don't like
        # the constructor having a different signature than that of the base class.
        sprite = cls(*groups)
        sprite.image = pygame.image.load(filename).convert_alpha()
        sprite.rect = sprite.image.get_rect()
        return sprite

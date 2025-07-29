from typing import Any, Sequence, Tuple, Union

import pygame

# imitate pygame types for type checking
RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[
    pygame.Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]
]
Coordinate = Union[Tuple[float, float], Sequence[float], pygame.math.Vector2]


class CircleSprite(pygame.sprite.Sprite):
    """
    A CircleSprite must be given a color, center, and radius.
    This is analogous to the pygame.draw.circle function for drawing a circle.
    It's recommended to use the `create` class method to instantiate this sprite.
    """

    color: ColorValue
    center: Coordinate
    radius: float
    rect: pygame.Rect
    image: pygame.Surface

    def __init__(self, *groups: Any) -> None:
        super().__init__(*groups)
        self.color = (0, 0, 0)
        self.center = (0, 0)
        self.radius = 0.0

    @classmethod
    def create(cls, color, center, radius, *groups):
        # This is done as a classmethod, not in the constructor,
        # to keep type checkers happy since they don't like
        # the constructor having a different signature than that of the base class.
        sprite = cls(*groups)
        sprite.color = color
        sprite.center = center
        sprite.radius = radius
        sprite.update()
        return sprite

    def update(self) -> None:
        # TODO: Improve performance by only updating if needed?
        #  (i. e., color, center, or radius changes)
        self.rect = pygame.Rect(
            self.center[0] - self.radius,
            self.center[1] - self.radius,
            self.radius * 2,
            self.radius * 2,
        )
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        pygame.draw.circle(
            self.image, self.color, (self.radius, self.radius), self.radius
        )
        self.image.convert_alpha()

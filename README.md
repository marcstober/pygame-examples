# Pygame Examples

Example code used in teaching Python with Pygame.

## Contents

-   **[recipes/](recipes/)**  
    Minimal, focused Pygame examples ("recipes") for specific tasks, such as displaying images, drawing text, and handling timed events. See [`recipes/README.md`](recipes/README.md) for details.

-   **[sprite/](sprite/)**  
    Reusable sprite classes ( [`RectSprite`](sprite/rectsprite.py), [`CircleSprite`](sprite/circlesprite.py), and[`ImageSprite`](sprite/imagesprite.py)) and additional related examples. (See also TODO below.)

-   **[tw/](tw/)**  
    Transition warning program ([`tw.py`](tw/tw.py)) used, for example, to display a countdown of work time remaining in a classroom. Also an example of a Pygame app.

-   **[mrrectangle.py](mrrectangle.py)**  
    "Mr. Rectangle" game. Complete example that demonstrates importing sprites, a sprite with an image, collision detection, drawing text, setting a window caption, game over/restart logic, and a timer.

-   **[rocketlander.py](rocketlander.py)**  
    "Rocket Lander" game. Complete example that demonstrates using masks to detect collisions of a `CircleSprite` with an `ImageSprite` with an arbitrary shape and transparent background.

-   **[sprite-example.py](sprite-example.py)**  
    Basic, single-file example of sprite creation, movement with keyboard input, and using a sprite `update` method.

-   **[sprite-shape-example.py](sprite-shape-example.py)**  
    Single-file example with circle collision detection using masks.

-   **[pygame-widgets-example.py](pygame-widgets-example.py)**  
    Example of using the `pygame-widgets` library to add a button and text box to a Pygame window.

-   **[smoketest.py](smoketest.py)**  
    This is not as an example itself, but used to [smoke test](<https://en.wikipedia.org/wiki/Smoke_testing_(software)>) all the examples in this project.

## TODO

-   Add a music player recipe.
-   The idea of `CircleSprite`, `RectSprite`, and `ImageSprite` in the `sprite` directory is that these could be packaged so learners can use these sprites without having to write a class. I.e., they could add to their code:

```
import spritefactory
```

And then:

```
spritefactory.create.circle_sprite(color, center, radius)
```

It's intentional that the signature of that function, and even the structure of that whole line, is similar to drawing a circle without using a sprite, so learners can adapt their "non-sprite" code (i.e., `pygame.draw.circle(screen, color, center, radius)`) to use sprites if that would help with their project. (This assumes there is also a `create.py` module that is generated containing the `create` or equivalent class methods for instantiating the various types of sprites.)

## Credits

-   Rocket image from by [Guiseppe Ramos on Vecteezy](https://www.vecteezy.com/vector-art/49496512-pixel-rocket-ship-illustration). Edited to make background transparent and saved as PNG with [Photopea](https://www.photopea.com/). (I usually use [Paint.NET](https://www.getpaint.net/index.html) for this sort of thing, but thought an online editor might be easier than downloading an app for students just needing to make a quick edit.

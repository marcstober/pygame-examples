import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

the_text = "Hello, world!"


def on_btn_click(param):
    # print("clicked!")
    pygame.draw.rect(win, (0, 0, 0), (100, 300, 1000, 1000))  # clear output area
    # draw_text("You said: " + tb.getText(), 300)
    global the_text
    the_text = tb.getText()
    change_button_text(btn, "hi")


def draw_text(text, y=0):
    fnt = pygame.font.SysFont("Georgia", 20)
    txt = fnt.render(text, True, (255, 255, 255))
    win.blit(txt, txt.get_rect(x=100, y=y))


pygame.init()

size = (600, 400)
win = pygame.display.set_mode(size, pygame.RESIZABLE)

# add things to the screen

btn = Button(
    win, 100, 200, 200, 75, text="Click me", onClick=on_btn_click, onClickParams=(1,)
)

tb = TextBox(win, 100, 50, 400, 75)

draw_text("Enter some text:")

pygame.display.flip()


def change_button_text(button, text):
    """Change text on pygame-widgets button."""
    button.string = text
    button.text = button.font.render(button.string, True, button.textColour)


running = True
while running:  # event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

    win.fill((100, 100, 100))

    draw_text(the_text, 300)

    pygame_widgets.update(events)
    pygame.display.flip()

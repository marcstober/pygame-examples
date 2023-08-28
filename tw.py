import argparse
import math
import pygame
from datetime import datetime, date

# TODO: package so this is specified as a dependency?
from pysetwindowpos import set_window_topmost

PROMPT_TEXT = "enter time in %H:%M format and press enter to reset"

# colors = ((172, 172, 0), (0, 172, 0)) # default
colors = ((243, 113, 33), (18, 182, 202))  # Sci-Tech


def draw_text(surface, text):
    font = pygame.font.SysFont(None, 30)
    if text == PROMPT_TEXT:
        color = (128, 128, 128)
    else:
        color = (255, 255, 255)
    text = font.render(text, True, color)
    x = surface.get_width() / 2 - text.get_rect().w / 2
    surface.blit(text, (x, 200))


class TransitionWarningApp:
    def __init__(self):
        self.text = ""

    def _parse_time(self, time_arg):
        # FUTURE: use https://dateutil.readthedocs.io/en/stable/ ?
        parsed_time = datetime.strptime(time_arg, "%H:%M").time()
        end_time = datetime.combine(date.today(), parsed_time)
        return end_time

    def _get_minutes_remaining(self):
        tdelta = self.end_time - datetime.today()
        minutes = int(tdelta.total_seconds() / 60)
        return minutes

    def _reset(self, time_arg):
        self.end_time = self._parse_time(time_arg)
        self.size = math.ceil(math.sqrt(self._get_minutes_remaining()))
        print(self.end_time)

    def _handle_keydown(self, event):
        if self.text == PROMPT_TEXT:
            self.text = ""

        # H/T: https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
        if event.key == pygame.K_RETURN:
            self._reset(self.text)
            self.text = ""
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text += event.unicode

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("time")
        args = parser.parse_args()

        pygame.init()  # not always needed, but seems to be best practice?

        clock = pygame.time.Clock()
        self._reset(args.time)
        minutes = self._get_minutes_remaining()
        print(minutes)

        win = pygame.display.set_mode((600, 400))

        set_window_topmost(pygame.display.get_wm_info()["window"])

        # chime from https://www.wavsource.com/sfx/sfx.htm
        chime_sound = pygame.mixer.Sound("chime1.mabc.wav")
        chime_sound.play()
        out_sound = pygame.mixer.Sound("chime2.mabc.wav")
        out_sound.play()

        running = True
        chime_played = False
        out_played = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    self._handle_keydown(event)

            # whether or not there was an event
            win.fill((0, 0, 0))
            m = 0
            pygame.display.set_caption(f"{minutes} Minute Transition Warning")

            if minutes < 1:
                if not out_played:
                    out_sound.play()
                    out_played = True
                    self.text = PROMPT_TEXT

            else:
                if minutes < 5:
                    if not chime_played:
                        chime_sound.play()
                        chime_played = True

                color = colors[0]
                for i in range(0, self.size):
                    for j in range(0, self.size):
                        if m < minutes:
                            pygame.draw.rect(win, color, (j * 50, i * 50, 48, 48))
                        m += 1
                        if m == 5:
                            color = colors[1]

            draw_text(win, self.text)

            pygame.display.flip()

            minutes = self._get_minutes_remaining()

            clock.tick(24)


if __name__ == "__main__":
    TransitionWarningApp().run()

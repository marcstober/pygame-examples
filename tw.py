import argparse
import math
import pygame
from datetime import datetime, date

# TODO: package so this is specified as a dependency?
from pysetwindowpos import set_window_topmost


class TransitionWarningApp:
    def _parse_time(self, time_arg):
        # FUTURE: use https://dateutil.readthedocs.io/en/stable/ ?
        parsed_time = datetime.strptime(time_arg, "%H:%M").time()
        end_time = datetime.combine(date.today(), parsed_time)
        return end_time

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("time")
        args = parser.parse_args()

        pygame.init()  # not always needed, but seems to be best practice?

        clock = pygame.time.Clock()
        end_time = self._parse_time(args.time)
        print(end_time)
        tdelta = end_time - datetime.today()
        minutes = int(tdelta.total_seconds() / 60)
        print(minutes)

        size = math.ceil(math.sqrt(minutes))

        win = pygame.display.set_mode((600, 400))

        set_window_topmost(pygame.display.get_wm_info()["window"])

        # chime from https://www.wavsource.com/sfx/sfx.htm
        chime_sound = pygame.mixer.Sound("airplane_chime_x.wav")
        chime_sound.play()
        out_sound = pygame.mixer.Sound("out.WAV")
        out_sound.play()

        running = True
        chime_played = False
        out_played = False
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    break

            # whether or not there was an event
            win.fill((0, 0, 0))
            m = 0
            pygame.display.set_caption(f"{minutes} Minute Transition Warning")

            if minutes < 1:
                if not out_played:
                    out_sound.play()
                    out_played = True

            else:
                if minutes < 5:
                    if not chime_played:
                        chime_sound.play()
                        chime_played = True

                color = (172, 172, 0)
                for i in range(0, size):
                    for j in range(0, size):
                        if m < minutes:
                            pygame.draw.rect(win, color, (j * 50, i * 50, 48, 48))
                        m += 1
                        if m == 5:
                            color = (0, 172, 0)

            pygame.display.flip()

            tdelta = end_time - datetime.today()
            minutes = int(tdelta.total_seconds() / 60)

            # TODO: maybe this should be higher to respond to other events, just don't update display
            clock.tick(1)


if __name__ == "__main__":
    TransitionWarningApp().run()

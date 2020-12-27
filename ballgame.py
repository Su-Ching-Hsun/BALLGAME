from campy.gui.events.timer import pause
from breakoutgraphics2 import BreakoutGraphics, Start
import keyboard

FRAME_RATE = 1000 / 120   # 120 frames per second.
NUM_LIVES = 5


def main():
    start = Start()
    if keyboard.read_key() == "space":
        graphics = BreakoutGraphics()
        start.window.close()
        lives = NUM_LIVES
        while True:
            if lives <= 0:
                break
            else:
                pause(FRAME_RATE)
                graphics.reflect()
                graphics.move()
                graphics.remove_and_score()
                graphics.countlives()
                if graphics.ball.y >= graphics.window.height:
                    lives -= 1
                    graphics.reset_ball()
                    graphics.switch_off()

                if lives <= 0:
                    break
                finished = graphics.finished()
                if finished:
                    break


if __name__ == '__main__':
    main()
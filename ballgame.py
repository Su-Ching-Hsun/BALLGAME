from campy.gui.events.timer import pause
from b2 import BreakoutGraphics

FRAME_RATE = 1000 / 100   # 120 frames per second.
NUM_LIVES = 10


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        if lives <= 0:
            break
        else:
            pause(FRAME_RATE)
            graphics.move()
            graphics.reflect()
            graphics.remove_and_point()
            graphics.window.remove(graphics.life)
            graphics.life.text = "Lives: " + str(lives)
            graphics.window.add(graphics.life)
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.window.remove(graphics.life)
                graphics.life.text = "Lives: " + str(lives)
                graphics.window.add(graphics.life)
                graphics.reset_ball()
                graphics.switch_off()

            if lives <= 0:
                break
            finished = graphics.finished()
            if finished:
                break


if __name__ == '__main__':
    main()
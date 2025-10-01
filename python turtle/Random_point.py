from setup import setup, get_pen
import turtle
import math
import colorsys
from random import randint


def int_to_rgb(hue: int, saturation: float = 1.0, value: float = 1.0):
    h = (hue % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(h, saturation, value)

    return r, g, b


def Random_point(pen, screen):

    steps = 200

    for i in range(steps):
        x = randint(
            int(-screen.window_width() / 2),
            int(screen.window_width() / 2)
            )
        y = randint(
            int(-screen.window_height() / 2),
            int(screen.window_height() / 2)
            )
        pen.goto(x, y)

        # color choice
        (x, y) = pen.pos()
        # color_pic = int(x - y)
        color_pic = randint(0, 360)

        pen.dot(5, int_to_rgb(color_pic))


    pen.up()
    pen.home()


def main(repeat=True):
    screen = setup()
    pen = get_pen()

    while True:
        Random_point(pen, screen)
        pen.clear()

    screen.exitonclick()


if __name__ == "__main__":

    main()

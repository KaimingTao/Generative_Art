from setup import setup, get_pen
import turtle
import math
import colorsys
from random import randint


def int_to_rgb(hue: int, saturation: float = 1.0, value: float = 1.0):
    h = (hue % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(h, saturation, value)

    return r, g, b


def Square_spiral(pen):

    steps = 100
    pen.pendown()
    step_length = 4
    turn = 92
    turn_move = 0.01
    pen.pensize(3)

    for i in range(steps):
        # color choice
        (x, y) = pen.pos()
        color_pic = int(x - y)
        # color_pic = randint(0, 360)

        pen.color(int_to_rgb(color_pic))

        # for j in range(i + 1):
        #     # color choice
        #     (x, y) = pen.pos()
        #     color_pic = int(x - y)
        #     # color_pic = randint(0, 360)

        #     pen.color(int_to_rgb(color_pic))

        #     pen.forward(step_length)

        pen.forward(i * step_length)
        pen.right(turn + i * turn_move)

    pen.up()
    pen.home()



def main(repeat=True):
    screen = setup()
    pen = get_pen()

    while True:
        Square_spiral(pen)
        pen.clear()

    screen.exitonclick()


if __name__ == "__main__":

    main()

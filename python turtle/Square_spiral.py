from setup import setup, get_pen
import turtle
import math


def Square_spiral(pen):

    steps = 100
    pen.pendown()
    step_length = 4
    turn = 92
    turn_move = 0.01

    for i in range(steps):
        pen.forward(i * step_length)
        pen.right(turn + i * turn_move)


    pen.up()

def main(repeat=True):
    screen = setup()
    pen = get_pen()

    while True:
        Square_spiral(pen)
        pen.clear()


    screen.exitonclick()


if __name__ == "__main__":

    main()


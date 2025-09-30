from setup import setup, get_pen
import turtle
import math

# https://en.wikipedia.org/wiki/Logarithmic_spiral

def Log_spiral(pen):

    a = 3
    k = 0.08

    steps = 1000
    pen.pendown()
    step_length = 4
    turn = 92
    turn_move = 0.01

    for i in range(steps):
        i = i / 10
        r = a * math.pow(math.e, k * i)
        x = r * math.cos(i)
        y = r * math.sin(i)
        pen.goto(x, y)
        pen.pendown()


    pen.up()

def main(repeat=True):
    screen = setup()
    pen = get_pen()

    while True:
        Log_spiral(pen)
        pen.clear()


    screen.exitonclick()


if __name__ == "__main__":

    main()


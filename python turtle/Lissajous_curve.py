from setup import setup, get_pen
import turtle
import math

# https://en.wikipedia.org/wiki/Lissajous_curve#In_engineering

def Lissajous_curve(pen):

    A = 200
    a = 1
    delta = math.pi / 2
    B = 100
    b = 3

    t = 0
    step_size = 0.01
    steps = 700

    for i in range(steps):
        t += step_size
        x = A * math.sin(a * t + delta)
        y = B * math.sin(b * t)
        pen.goto(x, y)
        pen.pendown()

    pen.up()

def main(repeat=True):
    screen = setup()
    pen = get_pen()

    while True:
        Lissajous_curve(pen)
        pen.clear()


    screen.exitonclick()



if __name__ == "__main__":

    main()


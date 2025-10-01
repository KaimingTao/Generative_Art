import turtle


def setup(width=500, height=500, bgcolor="white"):

    screen = turtle.Screen()
    screen.title("Simple Turtle Program")
    screen.bgcolor(bgcolor)
    screen.setup(width=width, height=height)

    return screen


def get_pen(size=1):
    pen = turtle.Turtle()
    pen.color("orange")
    pen.pensize(size)
    pen.penup()

    return pen

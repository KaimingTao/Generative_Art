
import turtle

def setup(bgcolor='white'):

    screen = turtle.Screen()
    screen.title("Simple Turtle Program")
    screen.bgcolor(bgcolor)
    screen.setup(width=500, height=500)

    return screen


def get_pen():
    pen = turtle.Turtle()
    pen.color("orange")
    pen.pensize(3)
    pen.penup()

    return pen

from pathlib import Path
from elements import Point, Line, Canvas
import random



def profile():
    width = 64
    height = 64
    canvas = Canvas(width, height)

    random.seed(int(time.time()))

    for i in range(2**24):
        p1 = Point(int(random.random() * width), int(random.random() * height))
        p2 = Point(int(random.random() * width), int(random.random() * height))
        if p1 == p2:
            continue

        line = Line(p1, p2, color=(
            int(random.random() * 255),
            int(random.random() * 255),
            int(random.random() * 255),
            ))
        line._draw(canvas.canvas)

    canvas.save(file_path="profile.png")


if __name__ == "__main__":
    profile()


# time python profile.py
# Mac M1: 319.90s user 0.50s system 99% cpu 5:20.95 total

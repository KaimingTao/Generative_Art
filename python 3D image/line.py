from PIL import Image
import numpy as np
from pathlib import Path


class Canvas:

    def __init__(self, width, height, color_mode="RGB", bg_color="white"):
        self.img = Image.new(color_mode, (width, height), bg_color)
        self.width = width
        self.height = height
        self.padding = 1
        self.canvas = self.img.load()

    def save(self, file_path=Path("pixels.png").resolve()):
        img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save(file_path)


class Point:

    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def transpose(self):
        return Point(self.y, self.x, self.color)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:

    def __init__(self, p1, p2, color=(0, 0, 0), transpose=False):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.transpose = transpose

    def draw(self, canvas):
        self.transform().assending()

        tan = abs(self.delta_y / self.delta_x) * 1.0

        error = 0
        x = int(self.p1.x)
        y = int(self.p1.y)

        delta_y = 1 if self.delta_y > 0 else -1
        # print(self.p1, self.p2)
        for x in range(int(self.p1.x), int(self.p2.x) + 1, 1):
            if error > 0.5:
                y = y + delta_y
                error -= 1.0

            # print(x, y)
            if self.transpose:
                canvas[y, x] = self.color
            else:
                canvas[x, y] = self.color

            error += tan

    def draw1(self, canvas):
        # Issue, not continous points
        for i in range(0, 100, 2):
            x = self.p1.x + (self.p2.x - self.p1.x) * i
            y = self.p1.y + (self.p2.y - self.p1.y) * 1
            canvas[x, y] = self.color

    def draw2(self, canvas):
        # Issue only for line abs(tan()) < 1
        # Issue, vertical line
        # Issue, If p2.x < p1.x
        for x in range(int(self.p1.x), int(self.p2.x) + 1):
            t = (x - self.p1.x) / (self.p2.x - self.p1.x)
            y = self.p1.y + (self.p2.y - self.p1.y) * t
            canvas[x, y] = self.color

    def draw3(self, canvas):
        # Issue only for line abs(tan()) < 1
        if (self.p1.x > self.p2.x):
            self.p1, self.p2 = self.p2, self.p1

        for x in range(int(self.p1.x), int(self.p2.x) + 1):
            t = (x - self.p1.x) / (self.p2.x - self.p1.x)
            y = self.p1.y + (self.p2.y - self.p1.y) * t
            canvas[x, y] = self.color

    def _draw(self, canvas):
        # Final version before optimization
        steep = abs(self.delta_x) < abs(self.delta_y)
        if steep:
            self.p1 = Point(self.p1.y, self.p1.x)
            self.p2 = Point(self.p2.y, self.p2.x)

        if (self.p1.x > self.p2.x):
            self.p1, self.p2 = self.p2, self.p1

        for x in range(int(self.p1.x), int(self.p2.x) + 1):
            t = (x - self.p1.x) / (self.p2.x - self.p1.x)
            y = self.p1.y + (self.p2.y - self.p1.y) * t

            if steep:
                canvas[y, x] = self.color
            else:
                canvas[x, y] = self.color

    @property
    def delta_x(self):
        return self.p2.x - self.p1.x

    @property
    def delta_y(self):
        return self.p2.y - self.p1.y

    def transform(self):
        if abs(self.delta_y) > abs(self.delta_x):
            self.transpose = True
            self.p1 = self.p1.transpose()
            self.p2 = self.p2.transpose()

        return self

    def assending(self):
        if self.p2.x < self.p1.x:
            self.p1, self.p2 = self.p2, self.p1

        return self


def parse_obj(file_path):
    vertices = []
    faces = []
    with open(file_path) as fd:
        for i in fd.readlines():
            if i.startswith("v "):
                vertices.append(i.split()[1:])
                continue

            if i.startswith("f "):
                faces.append(i.split()[1:])

    vertices = [(float(x), float(y), float(z)) for (x, y, z) in vertices]
    # print(vertices[0])
    vertices = {(idx + 1): v for idx, v in enumerate(vertices)}
    faces = [[int(v.split("/")[0]) for v in f] for f in faces]
    # print(faces[0])

    return {"vertices": vertices, "faces": faces}


def scale_point(v, scale):
    return (v + 1) / 2 * scale


def draw_obj(obj, canvas):
    vertices = obj["vertices"]

    for f in obj["faces"]:
        for i in range(len(f)):
            v1 = f[i]
            v2 = f[(i + 1) % len(f)]
            v1 = vertices[v1]
            v2 = vertices[v2]
            # print(v1, v2)
            # print(scale_point(v1[0], canvas.width), scale_point(v1[1], canvas.height))
            # print(scale_point(v2[0], canvas.width), scale_point(v2[1], canvas.height))
            p1 = Point(
                scale_point(v1[0], canvas.width - canvas.padding),
                scale_point(v1[1], canvas.height - canvas.padding),
            )
            p2 = Point(
                scale_point(v2[0], canvas.width - canvas.padding),
                scale_point(v2[1], canvas.height - canvas.padding),
            )
            line = Line(p1, p2)
            line._draw(canvas.canvas)


def work():

    width = 1000
    height = 1000

    canvas = Canvas(width, height)

    # line = Line(Point(13, 20), Point(80, 40))
    # line.draw(canvas.canvas)

    # line = Line(Point(20, 13), Point(40, 80))
    # line.draw(canvas.canvas)

    # line = Line(Point(20, 13), Point(40, 80), color=(255, 0, 0))
    # line.draw(canvas.canvas)

    obj = parse_obj(Path("./head.obj"))
    draw_obj(obj, canvas)

    canvas.save()


if __name__ == "__main__":
    work()

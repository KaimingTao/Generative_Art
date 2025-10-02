from PIL import Image
from pathlib import Path


class Canvas:

    def __init__(self, width, height, color_mode="RGB", bg_color="black"):
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

    def __eq__(self, p2):
        if self.x != p2.x:
            return False
        if self.y != p2.y:
            return False
        return True

    def copy(self):
        return Point(self.x, self.y, self.color)


class Line:

    def __init__(self, p1, p2, color=(0, 0, 0), transpose=False):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.transpose = False

    def draw(self, canvas):
        if abs(self.delta_y) > abs(self.delta_x):
            self.transpose = True
            self.p1 = self.p1.transpose()
            self.p2 = self.p2.transpose()

        if self.p2.x < self.p1.x:
            self.p1, self.p2 = self.p2, self.p1

        # tan = abs(self.delta_y / self.delta_x) * 1.0

        # print(self.p1, self.p2)

        y_error = 0
        y = int(self.p1.y)

        for x in range(int(self.p1.x), int(self.p2.x) + 1):
            if self.transpose:
                canvas[y, x] = self.color
            else:
                canvas[x, y] = self.color

            # https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
            # dx = 1
            # x1 = x0 + 1
            # ideal y1 = y0 + dy

            # the y point won't be at the accurate position

            # y_error always add dy, y_error += dy

            # 0.5 means the point is draw in the center of pixel.
            # if y_error <= 0.5 * dx, y1 = y0, y_error is still there, keep it
            # else, y1 = y0 + 1, y_error should minus 1 (dx), keep the remain error
            # then we can estimate error for each point

            # remove float 0.5
            # error operation is about
            # 2 * error <= 1 * dx (dx)
            # 2 * error += 2 dy
            # 2 * error -= 2 dx
            # because dy/dx = delta_y / delta_x
            # all operation can be scaled to delta y and delta x
            # and keey dy dx same sign as positive

            y_error += abs(2 * self.delta_y)
            if y_error > self.delta_x:
                y += 1 if self.delta_y > 0 else -1

                y_error -= 2 * self.delta_x

    def draw_zigzag(self, canvas):
        # algorithm from Nand2tetris
        a = 0
        b = 0
        diff = 0
        while (a <= self.delta_x) and (b <= self.delta_y):
            p1 = self.p1.copy()
            p1.x += a
            p1.y += b
            canvas[p1.x, p1.y] = self.color
            if diff < 0:
                a = a + 1
                diff = diff + self.delta_y
            else:
                b = b + 1
                diff = diff - self.delta_y

    def draw1(self, canvas):
        raise NotImplementedError
        # Issue, not continous points
        for i in range(0, 100, 2):
            x = self.p1.x + (self.p2.x - self.p1.x) * i
            y = self.p1.y + (self.p2.y - self.p1.y) * 1
            canvas[x, y] = self.color

    def draw2(self, canvas):
        raise NotImplementedError
        # Issue only for line abs(tan()) < 1
        # Issue, vertical line
        # Issue, If p2.x < p1.x
        for x in range(int(self.p1.x), int(self.p2.x) + 1):
            t = (x - self.p1.x) / (self.p2.x - self.p1.x)
            y = self.p1.y + (self.p2.y - self.p1.y) * t
            canvas[x, y] = self.color

    def draw3(self, canvas):
        raise NotImplementedError
        # Issue only for line abs(tan()) < 1
        if self.p1.x > self.p2.x:
            self.p1, self.p2 = self.p2, self.p1

        for x in range(int(self.p1.x), int(self.p2.x) + 1):
            t = (x - self.p1.x) / (self.p2.x - self.p1.x)
            y = self.p1.y + (self.p2.y - self.p1.y) * t
            canvas[x, y] = self.color

    def _draw(self, canvas):
        # raise NotImplementedError
        # Final version before optimization
        steep = abs(self.delta_x) < abs(self.delta_y)
        if steep:
            self.p1 = Point(self.p1.y, self.p1.x)
            self.p2 = Point(self.p2.y, self.p2.x)

        if self.p1.x > self.p2.x:
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


if __name__ == "__main__":
    width = 100
    height = 100

    canvas = Canvas(width, height)

    line = Line(Point(13, 20), Point(80, 40))
    line.draw(canvas.canvas)

    line = Line(Point(20, 13), Point(40, 80))
    line.draw(canvas.canvas)

    line = Line(Point(20, 13), Point(40, 80), color=(255, 0, 0))
    line.draw(canvas.canvas)

    canvas.save()

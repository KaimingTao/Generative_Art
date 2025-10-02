from elements import Line, Point, Canvas


class BoundingBox:

    def __init__(self, triangle):
        self.triangle = triangle
        self.min_x = min(int(triangle.p1.x), int(triangle.p2.x), int(triangle.p3.x))
        self.min_y = min(int(triangle.p1.y), int(triangle.p2.y), int(triangle.p3.y))
        self.max_x = max(int(triangle.p1.x), int(triangle.p2.x), int(triangle.p3.x))
        self.max_y = max(int(triangle.p1.y), int(triangle.p2.y), int(triangle.p3.y))

    def __repr__(self):
        return f"Bounding Box ({self.min_x}, {self.min_y}) => ({self.max_x}, {self.max_y})"


class Triangle:

    def __init__(self, p1, p2, p3, color=(255, 0, 0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.total_area = self.signed_area(self.p1, self.p2, self.p3)

        self.color = color

    def sort_vertices(self):
        # By y axis
        if self.p1.y > self.p2.y:
            self.p1, self.p2 = self.p2, self.p1

        if self.p1.y > self.p3.y:
            self.p1, self.p3 = self.p3, self.p1

        if self.p2.y > self.p3.y:
            self.p3, self.p2 = self.p2, self.p3

    def __call__(self, canvas):
        # self.sort_vertices()

        # self.draw_borderline(canvas, fill=False)
        # self.draw_borderline(canvas)

        # Method 2
        self.fill(canvas)

        # line12 = Line(self.p1, self.p2, self.color)
        # line12.draw(canvas)
        # line23 = Line(self.p2, self.p3, self.color)
        # line23.draw(canvas)
        # line31 = Line(self.p3, self.p1, self.color)
        # line31.draw(canvas)

    def signed_area(self, p1, p2, p3):
        # TODO use 1 to replace 1 should not change the result.
        # return 0.5 * (
        #     (p2.y - p1.y) * (p2.x + p1.x)
        #     + (p3.y - p2.y) * (p3.x + p2.x)
        #     + (p1.y - p3.y) * (p1.x + p3.x)
        # )
        return (
            (p2.y - p1.y) * (p2.x + p1.x)
            + (p3.y - p2.y) * (p3.x + p2.x)
            + (p1.y - p3.y) * (p1.x + p3.x)
        )

    def inside_triangle(self, p):
        # divided by total area to adjust the sign.
        # TODO: simplify this for integer operation
        area_a = self.signed_area(p, self.p1, self.p2) / self.total_area
        area_b = self.signed_area(p, self.p2, self.p3) / self.total_area
        area_c = self.signed_area(p, self.p3, self.p1) / self.total_area
        if area_a < 0:
            return False
        if area_b < 0:
            return False
        if area_c < 0:
            return False
        # print(p, area_a, area_b, area_c)
        return True

    def fill(self, canvas):
        # Use barycentric coordination

        if self.total_area < 0:
            return

        bounding_box = BoundingBox(self)
        # print(bounding_box, self.color)
        # print(self.p1, self.p2, self.p3)
        # print(self.signed_area(self.p1, self.p2, self.p3))

        for x in range(bounding_box.min_x, bounding_box.max_x + 1):
            for y in range(bounding_box.min_y, bounding_box.max_y + 1):
                if self.inside_triangle(Point(x, y)):
                    canvas[x, y] = self.color

    def draw_borderline(self, canvas, fill=True):

        if self.p1.y == self.p2.y:
            return

        segment_p1_p2 = self.p2.y - self.p1.y
        segment_p1_p3 = self.p3.y - self.p1.y
        segment_p2_p3 = self.p3.y - self.p2.y

        for y in range(self.p1.y, self.p2.y + 1):
            # left and right line start stop
            # TODO: use integer operation
            x1 = self.p1.x + ((self.p3.x - self.p1.x) * (y - self.p1.y)) / segment_p1_p3
            x2 = self.p1.x + ((self.p2.x - self.p1.x) * (y - self.p1.y)) / segment_p1_p2
            if fill:
                for x in range(int(min(x1, x2)), int(max(x1, x2)) + 1):
                    canvas[x, y] = self.color
            else:
                canvas[x1, y] = self.color
                canvas[x2, y] = self.color

        if self.p2.y == self.p3.y:
            return

        for y in range(self.p2.y, self.p3.y + 1):
            # left and right line start stop
            # TODO: use integer operation
            x1 = self.p1.x + ((self.p3.x - self.p1.x) * (y - self.p1.y)) / segment_p1_p3
            x2 = self.p2.x + ((self.p3.x - self.p2.x) * (y - self.p2.y)) / segment_p2_p3
            if fill:
                for x in range(int(min(x1, x2)), int(max(x1, x2)) + 1):
                    canvas[x, y] = self.color
            else:
                canvas[x1, y] = self.color
                canvas[x2, y] = self.color


def draw_triangle():
    canvas = Canvas(200, 200)

    tri1 = Triangle(
        Point(7, 45),
        Point(35, 100),
        Point(45, 60),
        (255, 0, 0),
    )
    tri1(canvas.canvas)
    tri2 = Triangle(
        Point(120, 35),
        Point(90, 5),
        Point(45, 110),
        (255, 255, 255),
    )
    tri2(canvas.canvas)
    tri3 = Triangle(
        Point(115, 83),
        Point(80, 90),
        Point(85, 120),
        (0, 255, 0),
    )
    tri3(canvas.canvas)

    canvas.save("Triangle.png")


if __name__ == "__main__":
    draw_triangle()

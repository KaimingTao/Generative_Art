from pathlib import Path
from elements import Point, Line, Canvas


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
            line.draw(canvas.canvas)


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

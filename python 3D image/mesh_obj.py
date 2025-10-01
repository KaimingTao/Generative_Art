from pathlib import Path
from elements import Point, Line, Canvas


def parse_obj(file_path):
    vertices = []
    faces = []
    with open(file_path) as fd:
        for i in fd.readlines():
            if i.startswith("v "):
                vertices.append(i.split()[1:4])
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
    # Originally the figure is in [-1, 1] ** 3, so need move to [0, 1] * scale
    # so (x + 1) / 2, then * scale
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
            line = Line(p1, p2, (10, 158, 245))
            line.draw(canvas.canvas)


def mesh_obj(obj_file):

    width = 1000
    height = 1000

    canvas = Canvas(width, height)

    obj = parse_obj(obj_file)
    draw_obj(obj, canvas)

    canvas.save(file_path=f"{obj_file.stem}.png")


if __name__ == "__main__":
    mesh_obj(Path("./head.obj"))
    mesh_obj(Path("./diablo3_pose.obj"))
    mesh_obj(Path("./body.obj"))

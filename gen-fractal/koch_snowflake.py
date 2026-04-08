"""Koch Snowflake fractal generator."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def koch_segment(p1, p2):
    """Return 4 points that replace a Koch curve segment."""
    d = p2 - p1
    p3 = p1 + d / 3
    p5 = p1 + 2 * d / 3
    # Rotate d/3 by 60 degrees
    angle = np.pi / 3
    rot = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
    p4 = p3 + rot @ (d / 3)
    return [p1, p3, p4, p5, p2]


def koch_snowflake(order=5):
    h = np.sqrt(3) / 2
    points = [np.array([0.0, h]),
              np.array([-0.5, 0.0]),
              np.array([0.5, 0.0]),
              np.array([0.0, h])]

    for _ in range(order):
        new_points = []
        for i in range(len(points) - 1):
            segment = koch_segment(np.array(points[i]), np.array(points[i + 1]))
            new_points.extend(segment[:-1])
        new_points.append(points[-1])
        points = new_points

    return np.array(points)


def main():
    print("Generating Koch Snowflake...")
    points = koch_snowflake(order=5)

    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
    ax.fill(points[:, 0], points[:, 1], color="#00aaff", alpha=0.7)
    ax.plot(points[:, 0], points[:, 1], color="#ffffff", linewidth=0.4)
    ax.set_aspect("equal")
    ax.set_title("Koch Snowflake (order 5)", fontsize=18, pad=12)
    ax.axis("off")
    fig.patch.set_facecolor("#0a0a2a")
    ax.set_facecolor("#0a0a2a")
    plt.tight_layout()
    plt.savefig("koch_snowflake.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print("Saved: koch_snowflake.png")


if __name__ == "__main__":
    main()

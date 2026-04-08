"""Sierpinski Triangle fractal generator using chaos game."""
import numpy as np
import matplotlib.pyplot as plt


def sierpinski_chaos_game(n_points=500_000):
    vertices = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2]])
    x, y = 0.5, 0.3
    xs, ys = [], []

    for _ in range(n_points):
        v = vertices[np.random.randint(3)]
        x = (x + v[0]) / 2
        y = (y + v[1]) / 2
        xs.append(x)
        ys.append(y)

    return np.array(xs), np.array(ys)


def main():
    print("Generating Sierpinski Triangle...")
    xs, ys = sierpinski_chaos_game()

    fig, ax = plt.subplots(figsize=(10, 9), dpi=100)
    ax.scatter(xs, ys, s=0.05, c=ys, cmap="plasma", linewidths=0, alpha=0.8)
    ax.set_aspect("equal")
    ax.set_title("Sierpinski Triangle", fontsize=18, pad=12)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("sierpinski_triangle.png", dpi=150, bbox_inches="tight",
                facecolor="black")
    print("Saved: sierpinski_triangle.png")


if __name__ == "__main__":
    main()

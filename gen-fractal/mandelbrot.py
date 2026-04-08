"""Mandelbrot Set fractal generator."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def mandelbrot(c, max_iter=256):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def generate_mandelbrot(width=1200, height=900, max_iter=256):
    x = np.linspace(-2.5, 1.0, width)
    y = np.linspace(-1.25, 1.25, height)
    result = np.zeros((height, width))

    for i, yi in enumerate(y):
        for j, xj in enumerate(x):
            result[i, j] = mandelbrot(complex(xj, yi), max_iter)

    return result


def main():
    print("Generating Mandelbrot Set...")
    data = generate_mandelbrot()

    colors = ["#000000", "#0d0221", "#190078", "#3d00a4", "#7b00d4",
              "#ff6600", "#ffcc00", "#ffffff"]
    cmap = LinearSegmentedColormap.from_list("mandelbrot", colors, N=512)

    fig, ax = plt.subplots(figsize=(12, 9), dpi=100)
    img = ax.imshow(data, cmap=cmap, extent=[-2.5, 1.0, -1.25, 1.25],
                    origin="lower", interpolation="bilinear")
    ax.set_title("Mandelbrot Set", fontsize=18, pad=12)
    ax.set_xlabel("Re(c)")
    ax.set_ylabel("Im(c)")
    plt.colorbar(img, ax=ax, label="Iterations to diverge")
    plt.tight_layout()
    plt.savefig("mandelbrot.png", dpi=150, bbox_inches="tight")
    print("Saved: mandelbrot.png")


if __name__ == "__main__":
    main()

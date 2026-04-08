"""Burning Ship fractal generator."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def burning_ship_iter(c, max_iter=256):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = (abs(z.real) + 1j * abs(z.imag)) ** 2 + c
    return max_iter


def generate_burning_ship(width=1200, height=900, max_iter=256):
    x = np.linspace(-2.5, 1.5, width)
    y = np.linspace(-2.0, 0.5, height)
    result = np.zeros((height, width))

    for i, yi in enumerate(y):
        for j, xj in enumerate(x):
            result[i, j] = burning_ship_iter(complex(xj, yi), max_iter)

    return result


def main():
    print("Generating Burning Ship fractal...")
    data = generate_burning_ship()

    colors = ["#000000", "#1a0000", "#660000", "#cc2200",
              "#ff8800", "#ffdd00", "#ffffff"]
    cmap = LinearSegmentedColormap.from_list("burning_ship", colors, N=512)

    fig, ax = plt.subplots(figsize=(12, 9), dpi=100)
    img = ax.imshow(data, cmap=cmap, extent=[-2.5, 1.5, -2.0, 0.5],
                    origin="lower", interpolation="bilinear")
    ax.set_title("Burning Ship Fractal", fontsize=18, pad=12)
    ax.set_xlabel("Re(c)")
    ax.set_ylabel("Im(c)")
    plt.colorbar(img, ax=ax, label="Iterations to diverge")
    plt.tight_layout()
    plt.savefig("burning_ship.png", dpi=150, bbox_inches="tight")
    print("Saved: burning_ship.png")


if __name__ == "__main__":
    main()

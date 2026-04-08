"""Julia Set fractal generator."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def julia(z, c, max_iter=256):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def generate_julia(c=-0.7269 + 0.1889j, width=1200, height=900, max_iter=256):
    x = np.linspace(-1.8, 1.8, width)
    y = np.linspace(-1.3, 1.3, height)
    result = np.zeros((height, width))

    for i, yi in enumerate(y):
        for j, xj in enumerate(x):
            result[i, j] = julia(complex(xj, yi), c, max_iter)

    return result


def main():
    # Classic beautiful Julia set constant
    c = -0.7269 + 0.1889j
    print(f"Generating Julia Set (c = {c})...")
    data = generate_julia(c=c)

    colors = ["#000000", "#1a0a3d", "#3d0080", "#8000ff", "#ff4400",
              "#ffaa00", "#ffff00", "#ffffff"]
    cmap = LinearSegmentedColormap.from_list("julia", colors, N=512)

    fig, ax = plt.subplots(figsize=(12, 9), dpi=100)
    img = ax.imshow(data, cmap=cmap, extent=[-1.8, 1.8, -1.3, 1.3],
                    origin="lower", interpolation="bilinear")
    ax.set_title(f"Julia Set  (c = {c})", fontsize=18, pad=12)
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    plt.colorbar(img, ax=ax, label="Iterations to diverge")
    plt.tight_layout()
    plt.savefig("julia_set.png", dpi=150, bbox_inches="tight")
    print("Saved: julia_set.png")


if __name__ == "__main__":
    main()

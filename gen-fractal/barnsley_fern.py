"""Barnsley Fern fractal generator using IFS (Iterated Function System)."""
import numpy as np
import matplotlib.pyplot as plt


# IFS coefficients: (a, b, c, d, e, f, probability)
BARNSLEY_IFS = [
    (0.00,  0.00,  0.00,  0.16, 0.00, 0.00, 0.01),  # stem
    (0.85,  0.04, -0.04,  0.85, 0.00, 1.60, 0.85),  # small leaflet
    (0.20, -0.26,  0.23,  0.22, 0.00, 1.60, 0.07),  # large left leaflet
    (-0.15, 0.28,  0.26,  0.24, 0.00, 0.44, 0.07),  # large right leaflet
]


def barnsley_fern(n_points=500_000):
    x, y = 0.0, 0.0
    xs, ys = [], []
    probs = [t[6] for t in BARNSLEY_IFS]
    cumprobs = np.cumsum(probs)

    for _ in range(n_points):
        r = np.random.random()
        idx = np.searchsorted(cumprobs, r)
        a, b, c, d, e, f, _ = BARNSLEY_IFS[idx]
        x, y = a * x + b * y + e, c * x + d * y + f
        xs.append(x)
        ys.append(y)

    return np.array(xs), np.array(ys)


def main():
    print("Generating Barnsley Fern...")
    xs, ys = barnsley_fern()

    fig, ax = plt.subplots(figsize=(8, 12), dpi=100)
    ax.scatter(xs, ys, s=0.05, c=ys, cmap="Greens", linewidths=0, alpha=0.8)
    ax.set_aspect("equal")
    ax.set_title("Barnsley Fern", fontsize=18, pad=12)
    ax.axis("off")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    plt.tight_layout()
    plt.savefig("barnsley_fern.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print("Saved: barnsley_fern.png")


if __name__ == "__main__":
    main()

"""Dragon Curve fractal generator using L-system."""
import numpy as np
import matplotlib.pyplot as plt


def dragon_curve_lsystem(order=15):
    """Generate Dragon Curve using L-system string expansion."""
    axiom = "FX"
    rules = {"X": "X+YF+", "Y": "-FX-Y"}
    seq = axiom
    for _ in range(order):
        seq = "".join(rules.get(ch, ch) for ch in seq)
    return seq


def lsystem_to_coords(seq, step=1.0):
    x, y = 0.0, 0.0
    angle = 0.0
    xs, ys = [x], [y]
    turn = np.pi / 2  # 90 degrees

    for ch in seq:
        if ch == "F":
            x += step * np.cos(angle)
            y += step * np.sin(angle)
            xs.append(x)
            ys.append(y)
        elif ch == "+":
            angle += turn
        elif ch == "-":
            angle -= turn

    return np.array(xs), np.array(ys)


def main():
    order = 14
    print(f"Generating Dragon Curve (order {order})...")
    seq = dragon_curve_lsystem(order)
    xs, ys = lsystem_to_coords(seq)

    # Color by segment index for gradient effect
    n = len(xs) - 1
    colors = np.linspace(0, 1, n)

    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
    for i in range(n):
        ax.plot(xs[i:i+2], ys[i:i+2],
                color=plt.cm.plasma(colors[i]), linewidth=0.5, alpha=0.9)

    ax.set_aspect("equal")
    ax.set_title(f"Dragon Curve (order {order})", fontsize=18, pad=12)
    ax.axis("off")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    plt.tight_layout()
    plt.savefig("dragon_curve.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print("Saved: dragon_curve.png")


if __name__ == "__main__":
    main()

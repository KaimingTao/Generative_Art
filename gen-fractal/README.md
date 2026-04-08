# Mathematical Fractals

A catalog of mathematical fractals organized by category, with Python generators for the most common ones.

---

## Categories

### 1. Escape-Time Fractals (Complex Plane)

Defined by iterating a complex function and measuring how quickly points diverge.

| Fractal | Formula | Notes |
|---|---|---|
| **Mandelbrot Set** | z → z² + c, z₀ = 0 | Most famous fractal; boundary is infinitely complex |
| **Julia Set** | z → z² + c, varying z₀ | Family of fractals; one per complex constant c |
| **Burning Ship** | z → (\|Re(z)\| + i\|Im(z)\|)² + c | Mandelbrot variant with absolute values |
| **Tricorn (Mandelbar)** | z → z̄² + c | Uses complex conjugate |
| **Newton Fractal** | Newton's method on polynomials | Basins of attraction for roots |
| **Multibrot Set** | z → zⁿ + c | Generalization with exponent n ≥ 2 |
| **Buddhabrot** | Mandelbrot with density rendering | Renders trajectory counts |
| **Phoenix Fractal** | z → z² + c + p·z_prev | Adds memory of previous iteration |

### 2. Iterated Function Systems (IFS)

Defined by a finite set of contractive affine transformations applied repeatedly.

| Fractal | Method | Notes |
|---|---|---|
| **Barnsley Fern** | IFS chaos game | Mimics natural fern leaf |
| **Sierpinski Triangle** | IFS / chaos game | Self-similar triangle |
| **Sierpinski Carpet** | IFS | 2D Cantor set analog |
| **Cantor Set** | Repeated middle-third removal | Simplest fractal |
| **Cantor Dust** | 2D Cantor set | Product of two Cantor sets |
| **Lévy C Curve** | IFS | Self-similar curve |
| **Heighway Dragon** | IFS | Same as Dragon Curve |
| **Menger Sponge** | IFS in 3D | 3D Sierpinski carpet analog |

### 3. L-System Fractals (Rewriting Systems)

Produced by recursive string rewriting rules interpreted as turtle graphics.

| Fractal | Axiom / Rule | Notes |
|---|---|---|
| **Dragon Curve** | FX → X+YF+, Y → −FX−Y | Repeatedly folded paper |
| **Koch Snowflake** | F → F+F−−F+F | Infinite perimeter, finite area |
| **Koch Curve** | Single segment variant | Building block of snowflake |
| **Hilbert Curve** | Space-filling curve | Visits every point in a square |
| **Peano Curve** | Space-filling curve | First known space-filling curve |
| **Gosper Curve** | Hexagonal variant | Also "flowsnake" |
| **Sierpinski Arrowhead** | L-system version of Sierpinski | Triangle via curve |
| **Plant / Tree Fractals** | Branching L-systems | Simulate botanical growth |

### 4. Self-Similar Geometric Fractals

Constructed by geometric subdivision rules.

| Fractal | Dimension | Notes |
|---|---|---|
| **Sierpinski Triangle** | ≈1.585 | Most studied self-similar fractal |
| **Koch Snowflake** | ≈1.262 | Infinite perimeter, finite area |
| **Apollonian Gasket** | ≈1.306 | Recursively packed circles |
| **Pythagoras Tree** | ~2 | Self-similar binary tree |
| **T-Square Fractal** | 2 | Recursive square subdivision |
| **Vicsek Fractal** | ≈1.465 | Plus-sign subdivision |
| **Cesàro Fractal** | ~1.5 | Bent Koch-type curve |

### 5. Strange Attractors (Dynamical Systems)

Emerge from chaotic differential equations; fractal structure in phase space.

| Attractor | System | Notes |
|---|---|---|
| **Lorenz Attractor** | 3 coupled ODEs | Butterfly shape; classic chaos |
| **Rössler Attractor** | 3 coupled ODEs | Simpler than Lorenz |
| **Hénon Map** | 2D discrete map | Classic strange attractor |
| **Clifford Attractor** | Sine-based 2D map | Visually rich |
| **De Jong Attractor** | Sine/cosine 2D map | Parametric family |
| **Duffing Attractor** | Forced oscillator | Physical application |
| **Tinkerbell Map** | 2D complex-like map | Small but intricate |
| **Halvorsen Attractor** | 3D cyclic ODE | Symmetric structure |

### 6. Fractal Landscapes & Nature-Inspired

Used for procedural terrain and texture generation.

| Fractal | Technique | Notes |
|---|---|---|
| **Diamond-Square** | Midpoint displacement | Terrain heightmaps |
| **Perlin Noise** | Gradient noise | Clouds, terrain, textures |
| **Fractional Brownian Motion** | Summed octaves of noise | Statistical self-similarity |
| **Random Midpoint Displacement** | 1D/2D recursive | Coastline simulation |
| **DLA (Diffusion-Limited Aggregation)** | Random walk growth | Coral / lightning shapes |
| **Eden Model** | Cluster growth | Biological colony shapes |

### 7. Number-Theoretic & Algebraic Fractals

Arising from number theory and algebraic structures.

| Fractal | Origin | Notes |
|---|---|---|
| **Cantor Set** | Set theory | First "pathological" set |
| **Pascal's Triangle mod n** | Number theory | Sierpinski pattern emerges |
| **Stern–Brocot Tree** | Rational numbers | Fractal tree of fractions |
| **Farey Sequence** | Number theory | Mediants of fractions |
| **Takagi (Blancmange) Curve** | Analysis | Continuous, nowhere differentiable |
| **Weierstrass Function** | Analysis | First nowhere-differentiable function |

### 8. 3D & Higher-Dimensional Fractals

| Fractal | Notes |
|---|---|
| **Mandelbulb** | 3D analog of Mandelbrot set |
| **Mandelbox** | Box-fold / sphere-fold iteration |
| **Menger Sponge** | 3D Sierpinski carpet |
| **Quaternion Julia Set** | Julia set in ℍ (quaternions) |
| **Apollonian Sphere Packing** | 3D Apollonian gasket |
| **Jerusalem Cube** | Recursive cube fractal |

---

## Python Generators (Common Fractals)

The following scripts generate fractal images as PNG files.

### Requirements

```bash
pip install numpy matplotlib
```

### Generate all at once

```bash
python generate_all.py
```

### Individual scripts

| Script | Output | Description |
|---|---|---|
| `mandelbrot.py` | `mandelbrot.png` | Classic Mandelbrot set |
| `julia_set.py` | `julia_set.png` | Julia set (c = −0.7269 + 0.1889i) |
| `sierpinski_triangle.py` | `sierpinski_triangle.png` | Chaos game method |
| `koch_snowflake.py` | `koch_snowflake.png` | Order-5 Koch snowflake |
| `barnsley_fern.py` | `barnsley_fern.png` | IFS Barnsley fern |
| `dragon_curve.py` | `dragon_curve.png` | L-system, order 14 |
| `burning_ship.py` | `burning_ship.png` | Burning Ship escape-time fractal |

Run any script directly:

```bash
python mandelbrot.py
python julia_set.py
python sierpinski_triangle.py
python koch_snowflake.py
python barnsley_fern.py
python dragon_curve.py
python burning_ship.py
```

---

## Quick Reference: Fractal Dimensions

| Fractal | Hausdorff Dimension |
|---|---|
| Cantor Set | log 2 / log 3 ≈ 0.631 |
| Koch Snowflake boundary | log 4 / log 3 ≈ 1.262 |
| Sierpinski Triangle | log 3 / log 2 ≈ 1.585 |
| Mandelbrot boundary | 2 |
| Barnsley Fern | ≈ 1.9 |
| Menger Sponge | log 20 / log 3 ≈ 2.727 |
| Mandelbulb surface | ≈ 2.97 |

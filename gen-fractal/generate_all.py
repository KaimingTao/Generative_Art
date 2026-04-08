"""Run all fractal generators in sequence."""
import importlib
import sys
import os

SCRIPTS = [
    "mandelbrot",
    "julia_set",
    "sierpinski_triangle",
    "koch_snowflake",
    "barnsley_fern",
    "dragon_curve",
    "burning_ship",
]

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    for name in SCRIPTS:
        print(f"\n{'='*40}")
        mod = importlib.import_module(name)
        mod.main()
    print(f"\n{'='*40}")
    print("All fractals generated!")

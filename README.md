# 🌌 Cosmic Tree

An animated tree painted live with Python's `turtle` library. It grows level by level from an orange trunk to green twigs, blooms with pink and cyan blossoms, and stands over glowing golden rings under a twinkling night sky.

## Preview

<!-- Add a screenshot or GIF here, e.g. ![Cosmic Tree](cosmic_tree.gif) -->

## Features

- Recursive fractal tree with random branch angles and lengths
- Colour gradient from orange trunk to yellow to green branches (HSV colour space)
- Blossoms at every branch tip
- Roots and glowing rings at the base
- 200 twinkling stars on a dark navy sky
- Reproducible: the same random seed gives the same tree

## Requirements

- Python 3.8 or newer
- No extra packages. `turtle`, `math`, `random` and `colorsys` ship with Python.

## Run

```bash
python cosmic_tree_turtle.py
```

A window opens and the tree paints itself. Close the window to stop.

## Customize

| Setting | What it does |
| --- | --- |
| `MAX_DEPTH` | Number of branch levels (more means denser but slower) |
| `random.seed(42)` | Change the number for a different tree shape |
| `steps` in `paint_tree()` | Growth animation speed |
| `NUM_STARS` | Number of stars in the sky |

## How it works

1. The tree structure is generated first with a recursive `grow()` function.
2. `paint_tree()` draws the branches one level at a time, in small steps, so it looks like growing.
3. `paint_blossoms()` adds flowers at the branch tips.
4. A timer keeps redrawing the stars with random brightness for the twinkle effect.

## Author

**Hasnain Raza**
[LinkedIn](https://www.linkedin.com/in/hasnain-raza-b42377395) · [GitHub](https://github.com/razahas5656-droid)

Inspired by a cosmic tree animation I saw online and rebuilt from scratch in Python.

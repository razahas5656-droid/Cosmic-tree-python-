import turtle
import math
import random
import colorsys

# ---------- Setup ----------
random.seed(42)

screen = turtle.Screen()
screen.setup(width=1000, height=850)
screen.bgcolor("#03020c")
screen.title("Cosmic Tree")
screen.colormode(1.0)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

star_pen = turtle.Turtle()
star_pen.hideturtle()
star_pen.speed(0)
star_pen.penup()

BASE_X, BASE_Y = 0, -270


def hsv(h, s=0.85, v=1.0):
    return colorsys.hsv_to_rgb(h % 1.0, s, v)


# ---------- Stars ----------
NUM_STARS = 200
stars = [
    (
        random.randint(-490, 490),
        random.randint(-410, 410),
        random.choice([2, 2, 3, 4]),
        random.choice([0.6, 0.62, 0.9, 0.95, 0.08]),  # blue / pink / warm
    )
    for _ in range(NUM_STARS)
]


def draw_stars(twinkle=False):
    star_pen.clear()
    for x, y, size, hue in stars:
        brightness = random.uniform(0.35, 1.0) if twinkle else 0.8
        star_pen.goto(x, y)
        star_pen.dot(size, hsv(hue, 0.25, brightness))


# ---------- Rings (glowing pool under the tree) ----------
def draw_rings():
    cx, cy = BASE_X, BASE_Y - 8
    for i, a in enumerate([110, 170, 235, 310]):
        b = a * 0.24
        pen.penup()
        pen.pensize(1 if i % 2 else 2)
        pen.color(hsv(0.12, 0.9, 0.55 - i * 0.07))
        for k in range(0, 361, 4):
            ang = math.radians(k)
            x = cx + a * math.cos(ang)
            y = cy + b * math.sin(ang)
            pen.goto(x, y)
            pen.pendown()
        pen.penup()
        screen.update()


# ---------- Roots ----------
def draw_roots():
    for _ in range(26):
        angle = random.uniform(205, 335)
        length = random.uniform(25, 75)
        pen.penup()
        pen.goto(BASE_X, BASE_Y)
        pen.setheading(angle)
        pen.pensize(random.choice([1, 1, 2]))
        pen.color(hsv(random.uniform(0.07, 0.11), 0.9, random.uniform(0.6, 0.9)))
        pen.pendown()
        pen.forward(length)
        pen.right(random.uniform(-30, 30))
        pen.forward(length * 0.4)
    pen.penup()
    screen.update()


# ---------- Tree structure ----------
MAX_DEPTH = 8
branches = []   # each: dict(x0, y0, x1, y1, depth, width, color)
tips = []


def grow(x, y, angle, length, depth):
    x1 = x + length * math.cos(math.radians(angle))
    y1 = y + length * math.sin(math.radians(angle))
    t = depth / MAX_DEPTH
    # orange trunk -> yellow -> green twigs
    color = hsv(0.07 + 0.27 * min(1.0, t * 1.15), 0.95, 1.0)
    width = max(1, round((MAX_DEPTH - depth) * 1.1))
    branches.append(dict(x0=x, y0=y, x1=x1, y1=y1, depth=depth, width=width, color=color))
    if depth == MAX_DEPTH:
        tips.append((x1, y1))
        return
    if depth == 0:
        # trunk splits in two big limbs
        grow(x1, y1, angle + random.uniform(22, 30), length * 0.82, 1)
        grow(x1, y1, angle - random.uniform(22, 30), length * 0.82, 1)
        return
    for sign in (-1, 1):
        a = angle + sign * random.uniform(18, 34) + random.uniform(-5, 5)
        grow(x1, y1, a, length * random.uniform(0.74, 0.82), depth + 1)


grow(BASE_X, BASE_Y, 90, 115, 0)


# ---------- Paint the tree, level by level ----------
def paint_tree():
    steps = 6
    for depth in range(MAX_DEPTH + 1):
        level = [b for b in branches if b["depth"] == depth]
        for s in range(1, steps + 1):
            f0, f1 = (s - 1) / steps, s / steps
            for b in level:
                dx, dy = b["x1"] - b["x0"], b["y1"] - b["y0"]
                pen.penup()
                pen.goto(b["x0"] + dx * f0, b["y0"] + dy * f0)
                pen.pensize(b["width"])
                pen.color(b["color"])
                pen.pendown()
                pen.goto(b["x0"] + dx * f1, b["y0"] + dy * f1)
            pen.penup()
            screen.update()


# ---------- Blossoms ----------
def blossom(x, y):
    hue = random.choice([0.92, 0.94, 0.96, 0.52, 0.55, 0.9])
    for _ in range(random.randint(3, 6)):
        px = x + random.uniform(-9, 9)
        py = y + random.uniform(-9, 9)
        pen.goto(px, py)
        pen.dot(random.randint(4, 8), hsv(hue, random.uniform(0.35, 0.8), 1.0))
    pen.goto(x, y)
    pen.dot(3, "white")


def paint_blossoms():
    random.shuffle(tips)
    pen.penup()
    for i, (x, y) in enumerate(tips):
        blossom(x, y)
        if i % 6 == 0:
            screen.update()
    screen.update()


# ---------- Run ----------
draw_stars()
screen.update()
draw_rings()
draw_roots()
paint_tree()
paint_blossoms()


# ---------- Twinkle forever ----------
def twinkle():
    draw_stars(twinkle=True)
    screen.update()
    screen.ontimer(twinkle, 300)


twinkle()
screen.mainloop()

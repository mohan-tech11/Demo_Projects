from vpython import *
from math import sin, cos, pi

# ----------------------------------
# 3D ANIMATED DURGA MATA
# ----------------------------------

scene = canvas(
    title="Jai Mata Di - 3D Durga Mata",
    width=1000,
    height=750,
    background=vector(0.025, 0.005, 0.10)
)

scene.center = vector(0, 2, 0)
scene.camera.pos = vector(0, 3, 18)
scene.camera.axis = vector(0, -1, -18)

# Colors
gold = vector(1, 0.68, 0.08)
red = vector(0.85, 0.015, 0.08)
skin = vector(1, 0.69, 0.48)
blue = vector(0.2, 0.25, 0.85)
white = vector(1, 0.95, 0.8)

# ----------------------------------
# GLOWING HALO
# ----------------------------------

halo = ring(
    pos=vector(0, 3.6, -0.7),
    axis=vector(0, 0, 1),
    radius=2.0,
    thickness=0.09,
    color=gold,
    emissive=True
)

halo2 = ring(
    pos=vector(0, 3.6, -0.65),
    axis=vector(0, 0, 1),
    radius=1.75,
    thickness=0.035,
    color=white,
    emissive=True
)

# Decorative rays around the halo
rays = []

for i in range(32):
    angle = 2 * pi * i / 32

    x1 = 2.05 * cos(angle)
    y1 = 3.6 + 2.05 * sin(angle)

    x2 = 2.35 * cos(angle)
    y2 = 3.6 + 2.35 * sin(angle)

    ray = cylinder(
        pos=vector(x1, y1, -0.7),
        axis=vector(x2 - x1, y2 - y1, 0),
        radius=0.025,
        color=gold,
        emissive=True
    )

    rays.append(ray)

# ----------------------------------
# LOTUS PEDESTAL
# ----------------------------------

cylinder(
    pos=vector(0, -0.3, 0),
    axis=vector(0, 0.35, 0),
    radius=1.5,
    color=gold
)

for i in range(12):
    angle = 2 * pi * i / 12

    petal = ellipsoid(
        pos=vector(
            1.0 * cos(angle),
            0.0,
            0.8 * sin(angle)
        ),
        length=0.85,
        height=0.35,
        width=0.35,
        color=red
    )

    petal.rotate(
        angle=angle,
        axis=vector(0, 1, 0),
        origin=vector(0, 0, 0)
    )

# ----------------------------------
# BODY AND RED SAREE
# ----------------------------------

ellipsoid(
    pos=vector(0, 1.0, 0),
    length=1.4,
    height=2.0,
    width=0.8,
    color=red
)

# Golden saree decoration
for y in [0.35, 0.65, 0.95, 1.25]:
    ring(
        pos=vector(0, y, 0.43),
        axis=vector(0, 0, 1),
        radius=0.48,
        thickness=0.025,
        color=gold
    )

# ----------------------------------
# NECK
# ----------------------------------

cylinder(
    pos=vector(0, 2.0, 0),
    axis=vector(0, 0.35, 0),
    radius=0.19,
    color=skin
)

# ----------------------------------
# FACE
# ----------------------------------

ellipsoid(
    pos=vector(0, 2.75, 0.05),
    length=0.65,
    height=0.85,
    width=0.55,
    color=skin
)

# Hair
ellipsoid(
    pos=vector(0, 3.0, -0.12),
    length=0.78,
    height=0.85,
    width=0.55,
    color=vector(0.08, 0.025, 0.02)
)

# Face in front of hair
ellipsoid(
    pos=vector(0, 2.75, 0.28),
    length=0.59,
    height=0.76,
    width=0.32,
    color=skin
)

# Eyes
for x in [-0.17, 0.17]:
    ellipsoid(
        pos=vector(x, 2.82, 0.445),
        length=0.13,
        height=0.065,
        width=0.035,
        color=white
    )

    sphere(
        pos=vector(x, 2.82, 0.475),
        radius=0.028,
        color=vector(0.08, 0.03, 0.02)
    )

# Bindi
sphere(
    pos=vector(0, 3.02, 0.46),
    radius=0.055,
    color=red,
    emissive=True
)

# Nose
sphere(
    pos=vector(0, 2.72, 0.47),
    radius=0.045,
    color=skin
)

# Smile
curve(
    pos=[
        vector(-0.09, 2.59, 0.47),
        vector(0, 2.56, 0.49),
        vector(0.09, 2.59, 0.47)
    ],
    color=red,
    radius=0.012
)

# ----------------------------------
# GOLDEN CROWN
# ----------------------------------

cylinder(
    pos=vector(0, 3.15, 0.03),
    axis=vector(0, 0.12, 0),
    radius=0.38,
    color=gold
)

cone(
    pos=vector(0, 3.25, 0.03),
    axis=vector(0, 0.65, 0),
    radius=0.38,
    color=gold
)

sphere(
    pos=vector(0, 3.92, 0.03),
    radius=0.10,
    color=white,
    emissive=True
)

# Crown jewels
for x in [-0.23, -0.12, 0, 0.12, 0.23]:
    sphere(
        pos=vector(x, 3.31, 0.36),
        radius=0.045,
        color=red
    )

# ----------------------------------
# NECKLACES
# ----------------------------------

for y in [2.05, 1.95, 1.85]:
    for i in range(13):
        angle = pi * i / 12

        sphere(
            pos=vector(
                0.38 * cos(angle),
                y - 0.15 * sin(angle),
                0.38
            ),
            radius=0.045,
            color=gold
        )

# ----------------------------------
# MULTIPLE ARMS
# ----------------------------------

arms = []

arm_positions = [
    (-0.45, 1.85, -1.0, 0.45),
    (0.45, 1.85, 1.0, 0.45),
    (-0.48, 1.55, -1.4, -0.05),
    (0.48, 1.55, 1.4, -0.05),
    (-0.45, 1.25, -1.1, -0.45),
    (0.45, 1.25, 1.1, -0.45),
    (-0.35, 1.05, -0.65, -0.75),
    (0.35, 1.05, 0.65, -0.75)
]

for sx, sy, ex, ey in arm_positions:

    arm = cylinder(
        pos=vector(sx, sy, 0),
        axis=vector(ex - sx, ey - sy, 0),
        radius=0.105,
        color=skin
    )

    hand = sphere(
        pos=vector(ex, ey, 0),
        radius=0.14,
        color=skin
    )

    arms.append((arm, hand, sx, sy, ex, ey))

# ----------------------------------
# TRIDENT
# ----------------------------------

trident_x = -1.75

cylinder(
    pos=vector(trident_x, 0.1, 0),
    axis=vector(0, 3.4, 0),
    radius=0.045,
    color=gold
)

# Three prongs
for offset in [-0.22, 0, 0.22]:

    curve(
        pos=[
            vector(trident_x + offset, 3.2, 0),
            vector(trident_x + offset, 3.55, 0),
            vector(trident_x + offset * 1.5, 3.85, 0)
        ],
        color=gold,
        radius=0.045
    )

# ----------------------------------
# LION-INSPIRED COMPANION
# ----------------------------------

lion_color = vector(0.95, 0.55, 0.08)

# Body
ellipsoid(
    pos=vector(1.7, 0.25, 0),
    length=1.15,
    height=0.7,
    width=0.65,
    color=lion_color
)

# Head
sphere(
    pos=vector(2.35, 0.65, 0.05),
    radius=0.42,
    color=lion_color
)

# Mane
sphere(
    pos=vector(2.32, 0.72, -0.08),
    radius=0.48,
    color=gold
)

# Face
sphere(
    pos=vector(2.45, 0.68, 0.38),
    radius=0.30,
    color=lion_color
)

# Eyes
for x in [2.32, 2.51]:
    sphere(
        pos=vector(x, 0.78, 0.63),
        radius=0.045,
        color=vector(0.05, 0.02, 0.01)
    )

# Nose
sphere(
    pos=vector(2.45, 0.59, 0.67),
    radius=0.07,
    color=red
)

# Legs
for x in [1.35, 1.75, 2.05]:
    cylinder(
        pos=vector(x, -0.05, 0),
        axis=vector(0, -0.30, 0),
        radius=0.11,
        color=lion_color
    )

# ----------------------------------
# FLOATING LIGHT PARTICLES
# ----------------------------------

particles = []

for i in range(35):
    x = -3.5 + (i % 7) * 1.1
    y = -0.5 + (i // 7) * 1.2

    p = sphere(
        pos=vector(x, y, -1.2),
        radius=0.035,
        color=gold,
        emissive=True
    )

    particles.append((p, x, y))

# ----------------------------------
# ANIMATION
# ----------------------------------

t = 0

while True:
    rate(30)

    t += 0.035

    # Pulsating divine halo
    halo.radius = 2.0 + 0.06 * sin(t)
    halo2.radius = 1.75 + 0.04 * sin(t + 1)

    # Animate halo rays
    for i, ray in enumerate(rays):
        ray.color = (
            gold if sin(t * 2 + i * 0.4) > 0
            else white
        )

    # Gentle movement of the hands
    for arm, hand, sx, sy, ex, ey in arms:
        new_y = ey + 0.035 * sin(t + sx * 3)

        arm.axis = vector(ex - sx, new_y - sy, 0)
        hand.pos = vector(ex, new_y, 0)

    # Floating golden particles
    for p, x, y in particles:
        p.pos.y = y + 0.10 * sin(t + x)
        p.visible = sin(t * 2 + x + y) > -0.7

    # Gentle camera movement
    scene.camera.pos = vector(
        0.12 * sin(t * 0.3),
        3,
        18
    )

    scene.camera.axis = vector(
        -scene.camera.pos.x,
        -1,
        -18
    )
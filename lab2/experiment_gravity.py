
from view import *
from model import *


particles = []
masses = [1, 2, 4, 8]
for i in range(4):
    particles.append(Particle(masses[i], Vec(-11 + 2 * i, 9), Vec(0, 0), 0.3))

speeds = [0, 2, 4, 6]
for i in range(4):
    particles.append(Particle(1, Vec(1, 9), Vec(speeds[i], 0), 0.3))


def gravity(dt, particles):
    constant_gravitational_field(dt, particles, 10)


def label(text, u):
    c = to_canvas_coords(canvas, u)
    canvas.create_text(c.x, c.y, text=text, fill="grey")


for i in range(4):
    label(f"m={masses[i]}", Vec(-11 + 2 * i, 9.6))
label("v = 0, 2, 4, 6", Vec(1, 9.6))

timestep = 0.000005
simulation_loop(gravity, timestep, particles)
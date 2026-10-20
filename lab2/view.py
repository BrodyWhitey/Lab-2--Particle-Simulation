from tkinter import *
from model import *
import time

root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()




# Task (7/12): Draw on canvas

# Task (8/12): Define a new function to_canvas_coords(canvas, x)
def to_canvas_coords(canvas, u):
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()
    scale= height / 20
    x= width / 2 + scale * u.x
    y= height / 2 - scale * u.y
    return Vec(x,y)

#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)

def move_oval_to(canvas, o, u1, u2):
    v1 = to_canvas_coords(canvas, u1)
    v2 = to_canvas_coords(canvas, u2)
    canvas.coords(o, v1.x, v1.y, v2.x, v2.y)



# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):
    o = canvas.create_oval(0, 0, 10, 10, fill="blue")
    top_left, bottom_right = particle.bounding_box()
    move_oval_to(canvas, o, top_left, bottom_right)
    return o

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f,timestep, particles):
    ovals= []

    for i in range(len(particles)):
        ovals.append(create_oval(canvas, particles[i]))

        
    last_view_update= time.time()
    while True:
        f(timestep, particles)

        for i in range(len(particles)):
            particles[i].inertial_move(timestep)

        now= time.time()
        if now - last_view_update >= 1/30:
            last_view_update = now
            for i in range(len(particles)):
                top_left , bottom_right= particles[i].bounding_box()
                move_oval_to(canvas, ovals[i], top_left, bottom_right)
            canvas.update()

import tkinter as tk
from simpy_starlinetor.physics_starlinetor.vectors import *

def tk_create_oval(canvas : tk.Canvas, position : vector2d , radius : float) -> int:
    """
    Creates a new oval for a tk instance.
    Instead of the borders of the excribed square it uses the center and the radius.
    Returns the id. 
    """
    
    x0 = int(position.get_x() - radius)
    x1 = int(position.get_x() + radius)
    y0 = int(position.get_y() - radius)
    y1 = int(position.get_y() + radius)
    
    return canvas.create_oval(x0,y0,x1,y1)

def world_to_camera():
    """
    Turns world cords to camera cords
    """
    pass

def camera_to_world():
    """
    Turn camera cords to world cords
    """
    pass
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

def world_to_camera(world_point : vector2d, camera_position : vector2d, camera_zoom : float) -> vector2d:
    """
    Turns world cords to camera cords
    At 100% zoom the camera resolution to world coordinates is 1-1
    At 200% is 2-1 and at 50% is 1-2
    The camera position is the position of the camera in the world coordinates
    Note that this function does not care where the 0,0 of the camera is or the resolution
    Given a world position it is returned the camera position rounded
    """
    #By subtracting from the point vector the camera vector we get the position vector relative to the camera position
    point_camera : vector2d =  world_point.vector_addition(camera_position.scalar_multiplication(-1))
    #We scale the vector based on the zoom 
    point_camera.scalar_multiplication(camera_zoom)
    #return to closests integer
    return vector2d().from_x_y(round(point_camera.get_x()), round(point_camera.get_y))

def camera_to_world(camera_point : vector2d, camera_position : vector2d, camera_zoom : float) -> vector2d:
    """
    Turn camera cords to world cords
    At 100% zoom the camera resolution to world coordinates is 1-1
    At 200% is 2-1 and at 50% is 1-2
    The camera position is the position of the camera in the world coordinates
    Note that this function does not care where the 0,0 of the camera is or the resolution
    Given a camera position it is returned the world position not rounded
    """
    #scale down the vector based on the zoom
    #here is inverted because we are going backwards
    scaled_camera_point : vector2d = camera_point.scalar_multiplication(1/camera_zoom)
    #by adding the two vectors we get the world point
    world_point : vector2d = scaled_camera_point.vector_addition(camera_position)
    return world_point
    
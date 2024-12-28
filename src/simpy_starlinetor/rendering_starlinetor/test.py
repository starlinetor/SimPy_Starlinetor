from simpy_starlinetor.physics_starlinetor.vectors import vector2d
from simpy_starlinetor.rendering_starlinetor.rendering_utils import world_to_camera


print(world_to_camera(vector2d().from_x_y(120,120), vector2d().from_x_y(0,0), 1, vector2d().from_x_y(1920,1080)).get_components("x","y"))
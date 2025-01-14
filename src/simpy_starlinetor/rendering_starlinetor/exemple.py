from simpy_starlinetor.physics_starlinetor.vectors import *
from simpy_starlinetor.sim_objects_starlinetor.particles_starlinetor.particle import *
from simpy_starlinetor.rendering_starlinetor.particle_renderer import * 
from simpy_starlinetor.framerate_starlinetor.framerate import *

class gravity_sim():
    
    def __init__(self):
        self.g = -100
        self.delta_t = 1/3600
        self.particle_1 : particle = particle(position = vector2d.from_x_y(0,0), speed = vector2d.from_x_y(0,0), delta_t=self.delta_t)
        self.particles = [self.particle_1, 
                        particle(position = vector2d.from_x_y(-100,-100), speed = vector2d.from_x_y(0,0), delta_t=self.delta_t),
                        particle(position = vector2d.from_x_y(100,-100), speed = vector2d.from_x_y(0,0), delta_t=self.delta_t),
                        particle(position = vector2d.from_x_y(-100,100), speed = vector2d.from_x_y(0,0), delta_t=self.delta_t),
                        particle(position = vector2d.from_x_y(100,100), speed = vector2d.from_x_y(0,0), delta_t=self.delta_t),
                        ]
        self.pr2d = particle_renderer_2d(self.particles, vector2d().from_x_y(1920,1080), 10)
    
    def start(self):
        return
    
    def loop(self):
        self.particle_1.add_acceleration(vector2d.from_x_y(0,-self.g))
        self.particle_1.update()
    
    def end(self):
        self.pr2d.update()

gravity_sim_1 = gravity_sim()

fh = frame_handler(main_class = gravity_sim_1, target_fps = 60, executions_pf = 60, fps_precision = 1)

while True:
    fh.basic()
from simpy_starlinetor.sim_objects_starlinetor.particles_starlinetor.particle import *
import simpy_starlinetor.framerate_starlinetor.framerate as fr
from simpy_starlinetor.physics_starlinetor.vectors import *

class gravity_sim():
    
    def __init__(self):
        self.g = 9.8
        self.delta_t = 1/3600
        self.particle_1 : particle.particle = particle.particle(position = vector2d.from_x_y(0,10), speed = vector2d.from_x_y(10,10), delta_t=self.delta_t)
    
    def start(self):
        return
    
    def loop(self):
        self.particle_1.add_acceleration(vector2d.from_x_y(0,-self.g))
        self.particle_1.update()
    
    def end(self):
        x,y = gravity_sim_1.particle_1.position.get_components("x","y")
        if y > 0:
            print(round(x,2),round(y,2))
        else : 
            self.g = 0
        

gravity_sim_1 = gravity_sim()

fh = fr.frame_handler(main_class = gravity_sim_1, target_fps = 60, executions_pf = 60, fps_precision = 1)

while True:
    fh.basic()
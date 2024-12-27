import tkinter as tk
from simpy_starlinetor.physics_starlinetor.vectors import *
from simpy_starlinetor.rendering_starlinetor.rendering_utils import *
from simpy_starlinetor.sim_objects_starlinetor.particles_starlinetor.particle import *

class particle_renderer_2d:
    
    def full_screen(self, eventorigin):
        self.full_screen_var = not self.full_screen_var
        self.root.attributes("-fullscreen",self.full_screen_var)
    
    def __init__(self, particles : list[particle], resolution : vector2d, particle_radius : float):
        """
        Functionality:
        R to reset to 0/0 and 100% zoom
        TODO Zoom : starting zoom is 100%
            scroll wheel 
        TODO Move around : ability to move around, this needs some type of chamera position
            left click drag
        TODO Adaptive resolution : this means that the rendering will be separated from the resolution
        TODO Render particles : draws circle where particles should be
        F11 -> full screen
        """
        #rendering variables
        self.particles : list[particle] = particles
        self.camera : vector2d = vector2d().from_x_y(0,0)
        #at 100% zoom the resolution is fully rappresented. 
        self.zoom : int = 100
        #this rappresents the radius of particles, is based on the simulation size and not rendering size
        self.particle_radius : float = particle_radius
        #full screen
        self.full_screen_var = True
        
        #initialize tk
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, bg="white",height=1080, width=1920)
        self.canvas.pack()
        
        #mapping of all keys
        #f11 fullscreen
        self.root.bind("<F11>", self.full_screen)
        
        #initialize particles
        #stores the id of each particle
        self.tk_particles : list[int] = []

        for _ in self.particles:
            self.tk_particles.append(tk_create_oval(self.canvas, vector2d(), self.particle_radius))
    
    def update(self):
        """"
        Renders the new frame
        """
        #TODO WIT
        #move particles
        for i in range(len(self.particles)):
            self.canvas.moveto( self.tk_particles[i],
                                self.particles[i].get_position().get_x() - self.particle_radius,
                                self.particles[i].get_position().get_y() - self.particle_radius)
        #update canvas
        self.root.update()
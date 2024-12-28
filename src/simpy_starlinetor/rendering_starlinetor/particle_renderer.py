import tkinter as tk
from simpy_starlinetor.physics_starlinetor.vectors import *
from simpy_starlinetor.rendering_starlinetor.rendering_utils import *
from simpy_starlinetor.sim_objects_starlinetor.particles_starlinetor.particle import *

class particle_renderer_2d:
    
    def full_screen(self, eventorigin):
        """
        Sets the screen to full screen
        """
        self.full_screen_var = not self.full_screen_var
        self.root.attributes("-fullscreen",self.full_screen_var)
    
    def reset_camera(self, eventorigin):
        """
        Resets the camera to 0,0 and to 100% zoom
        """
        self.camera = vector2d()
        self.zoom = 1
        self.zoom_changed = True
    
    def edit_zoom(self, event):
        """
        Changes the zoom
        """
        self.zoom *= math.pow(2 , event.delta / 120 )
        #a bit of optimization
        self.zoom_changed = True
        #doubles or divides the zoom
    
    def __init__(self, particles : list[particle], resolution : vector2d, particle_radius : float):
        """
        Functionality:
        R to reset to 0/0 and 100% zoom
        mouse wheel to edit the zoom
        TODO Move around : ability to move around, this needs some type of chamera position
            left click drag
        TODO Render particles : draws circle where particles should be
        F11 -> full screen
        """
        #rendering variables
        self.particles : list[particle] = particles
        self.camera : vector2d = vector2d().from_x_y(0,0)
        #at 100% zoom the resolution is fully rappresented. 
        self.zoom : float = 1
        self.zoom_changed : bool = False
        #this rappresents the radius of particles, is based on the simulation size and not rendering size
        self.particle_radius : float = particle_radius
        #full screen
        self.full_screen_var = True
        #resolution
        self.resolution : vector2d = resolution
        
        #initialize tk
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, bg="white",height=resolution.get_y(), width=self.resolution.get_x())
        self.canvas.pack()
        self.root.attributes("-fullscreen",self.full_screen_var)
        
        #mapping of all keys
        #f11 fullscreen
        self.root.bind("<F11>", self.full_screen)
        #r reset
        self.root.bind("<r>", self.reset_camera)
        #scroll wheel -> zoom
        self.root.bind("<MouseWheel>", self.edit_zoom)
        
        #initialize particles
        #stores the id of each particle
        self.tk_particles : list[int] = []

        for _ in self.particles:
            self.tk_particles.append(tk_create_oval(self.canvas, vector2d(), self.particle_radius))
    
    def update(self):
        """"
        Renders the new frame
        """
        
        self.resolution = vector2d().from_x_y(self.canvas.winfo_width(), self.canvas.winfo_height())
    
        #move particles
        for i in range(len(self.particles)):
            #get camera cords from world cords
            particle_camera_cords : vector2d = world_to_camera( self.particles[i].get_position(),
                                                                self.camera,
                                                                self.zoom,
                                                                self.resolution
                                                                )
            #move objects
            self.canvas.moveto( self.tk_particles[i],
                                particle_camera_cords.get_x() - self.particle_radius * self.zoom,
                                particle_camera_cords.get_y() - self.particle_radius * self.zoom)
            #resize objects
            if self.zoom_changed:
                resize_oval(self.canvas,self.tk_particles[i], self.particle_radius, self.zoom)
        #set zoom changed to false
        self.zoom_changed = False
        #update canvas
        self.root.update()
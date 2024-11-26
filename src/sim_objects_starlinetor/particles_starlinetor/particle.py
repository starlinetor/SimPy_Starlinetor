from physics_starlinetor.vectors import vector2d

class particle:
    """
    Basic particle with only position, speed, acceleration and force as parameters\n
    Mass is an optional parameter, if unused use acceleration only instead of the force
    """
    #class variables
    def __init__(self, position : vector2d, speed : vector2d, delta_t : float, mass = 0):
        self.position = position
        self.speed = speed
        self.mass = mass
        self.delta_t = delta_t
        #these values are only used to calculate how the particle will behave in the next frame
        #these are not supposed to be modified directly or acessed in any way 
        self.acceleration = vector2d.from_x_y(0,0)
        self.force = vector2d.from_x_y(0,0)

    def add_force(self, force : vector2d):
        """
        Adds a force to the particle
        """
        self.force.vector_addition(force)
    
    def add_acceleration(self, acceleration : vector2d):
        """
        Adds an acceleration to the particle
        """
        self.acceleration.vector_addition(acceleration)
    
    def update_acceleration_only(self):
        """
        This function updates position and speed using acceleration only.\n
        update() calls this function by default if the mass is 0
        """
        # delta v = v + a * delta t
        print(self.acceleration.components)
        self.acceleration.scalar_multiplication(self.delta_t)
        print(self.acceleration.components)
        #TODO this is not adding stuff
        self.speed.vector_addition(self.acceleration)
        print(self.speed.components)
        # delta x = x + v * delta t
        self.speed.scalar_multiplication(self.delta_t)
        self.position.vector_addition(self.speed)
        #clear vectors
        self.force.clear_vector()
        self.acceleration.clear_vector()
        
    def update(self):
        """
        Function to be called at the end of a frame to update the particle position and speed
        """
        if self.mass == 0: 
            self.update_acceleration_only()
        else:
            #total a = a + total force / m
            self.acceleration.vector_addition(self.force.scalar_multiplication(1/self.mass))
            self.update_acceleration_only()

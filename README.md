Multi pourpose functions for simulations

# framerate_starlinetor
Frame rate handling

## framerate
This class allows you to make a frame_handler object that helps you execute programs that need some sort of framerate. 
To use it just create a class where all your code will be in. This class must have 3 functions. 

### start
This function is executed at the start of each frame

### loop
This function is executed many times each frame.
You can chose how many by editing the "executions_pf" parameter when creating the frame_handler class. 

### end 
This function is executed at the end of a frame.

Now instantiate your main class and instatiate the frame_handler with reference to istantiated class. 
Then create a while loop and inside run framerate."chose function()". These are the available options

### basic
This will execute your code following your taget_fps parameter. But if the code is too slow it will just slow down. 

# physics_starlinetor
Useful physics related utilities

## vector2d
Basic 2d vectors

### Initialization
from_x_y : enter the x and y component
from_module_angle : enter a module and an angle. Angles are in radiant. 0 is to the right, pi/2 is to the top. 

### getters
get_components : takes as argument the name of a component - for 2d vectors the defaults are "x" and "y" and returns theyr value
get_module : returns the module
get_angle_2d : specific for the vector 2d, returns the angle, works the same as the initialization

#setters
set_x_y
set_module_angle
clear_vector : sets all the components to zero

#vectors operations
vector_addition : adds a vector to the vector (instance function)
scalar_multiplication : multiplies a vector by a scalar (instance function)

# sim_objects_starlinetor
A bunch of usefull objects for physics simulations.
Each object has an update() and "yet to be defigned" functions.

### update()
Used at the end of a simulation step to update the object

### yet to be defigned
Used during a simulation step. This function dictates what the object does during the simulation step.
For exemple a proton in this function would apply a force to all other charged particles. 

## particle
A basic block for creating any particle simulation. 

## container
A container for particles. 


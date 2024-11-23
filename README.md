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

# sim_objects_starlinetor
A bunch of usefull objects for physics simulations.

## particle
A basic block for creating any particle simulation. 

## container
A container for particles. 


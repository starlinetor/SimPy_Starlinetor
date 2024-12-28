import math
from simpy_starlinetor.physics_starlinetor.vectors import * 

#empty vector
speed = vector2d()
print(speed.components)

#declared x and y vector
speed = vector2d.from_x_y(x = 0, y = 1)
print(speed.components)

#declared module and angle vector
speed = vector2d.from_module_angle(module = 10, angle = math.pi)
print(speed.components)

#get components
print(speed.get_components("x", "y"))

print(speed.get_module())

print(speed.get_angle_2d())

#set components
speed.set_components(("x",10),("y",23))
print(speed.components)

#set module angle
speed.set_module_angle(10,6)
print(speed.components)

print(speed.vector_addition(vector2d.from_x_y(5,5)).components)

print(speed.scalar_multiplication(10).components)
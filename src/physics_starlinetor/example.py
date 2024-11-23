import math
from vectors import vector2d

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
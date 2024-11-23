from vectors import vector2d

#empty vector
speed = vector2d()
print(speed.components)

#declared x and y vector
speed = vector2d.from_x_y(x = 10, y = 1)
print(speed.components)

#declared module and angle vector
speed = vector2d.from_module_angle(module = 10, angle = 4)
print(speed.components)

#get components
print(speed.get_components("x", "y"))
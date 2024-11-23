import math

from numpy import append


class vector2d:
    
    #data
    components : dict[str:float] = {}
    
    #builders
    def __init__(self):
        """
        Empty vector
        """
        self.components["x"] = 0
        self.components["y"] = 0
    
    @classmethod
    def from_x_y(cls, x : float = 0, y : float = 0):
        """
        Vector declared using x and y components
        """
        vector = cls()
        vector.components["x"] = x
        vector.components["y"] = y
        return vector
    
    @classmethod    
    def from_module_angle(cls, module : float = 0 , angle : float = 0):
        """
        Vector declared using module and angle
        """
        vector = cls()
        vector.components["x"] = module * math.cos(angle)
        vector.components["y"] = module * math.sin(angle)
        return vector
    
    #getters
    def get_components(self,*keys : str) -> list[float]:
        components_list : list[float] = []
        for key in keys:
            components_list.append(self.components[key])
        return components_list
import math

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
    #components
    def get_components(self,*keys : str) -> tuple[float]:
        """
        Returns the value of the components of the vector\n
        Uses the name of each component as the parameter
        """
        components_list : list[float] = []
        for key in keys:
            components_list.append(self.components[key])
        return tuple(components_list)
    
    #module
    def get_module(self) -> float:
        """
        Returns the module of the vector, works for any n dimension vector
        """
        module = math.sqrt(sum(map(lambda i: i * i, self.components.values())))
        return module
    
    def get_angle_2d(self) -> float:
        """
        Returns the angle of a 2d vector
        """
        #atan2 is already robust against division by zero
        angle = math.atan2(self.components["y"],self.components["x"])
        return angle
    
    def set_components(self,*keys_values : tuple[str | float]):
        """
        Sets the components of the vector
        ## parameters
        ### keys_values : tuple 
        first value is the key of a component\n
        second value is the value of the component
        """
        
        for x,y in keys_values:
            if x not in self.components.keys():
                raise ValueError(f"{x} is not a component in the vector")
            if not isinstance(y,float) and not isinstance(y,int):
                raise ValueError(f"{y} should be type float or int not {type(y)}")
            self.components[x] = y
            
    def set_module_angle(self, module : float = 0 , angle : float = 0):
        """
        Set module and angle of a vector
        """
        self.components["x"] = module * math.cos(angle)
        self.components["y"] = module * math.sin(angle)
        return self
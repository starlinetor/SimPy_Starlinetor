class vector2d:
    
    components : dict[str:float] = {
        "x" : 0,
        "y" : 0
    }
    
    def __init__(self, x : float, y : float):
        self.components["x"] = x
        self.components["y"] = y
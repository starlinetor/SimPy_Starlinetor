from framerate import frame_handler

class exemple_class :
    
    i : int = None
    fr : frame_handler = None
    
    def __init__(self):
        self.i = 0
        
    def get_frame_handler(self, fr : frame_handler):
        #get the fr to find the avrage fps
        self.fr = fr
    
    def start(self):
        #executed at the start of the frame
        print("Starting frame")
    
    def loop(self):
        #executed many times in a frame
        self.i +=1
    
    def end(self):
        #executed at the end of a frame
        print("Frame executed")
        print(f"i : {self.i}")
        print(f"Avrage fps : {fr.average_fps()}, Avrage spf : {fr.average_spf()}")

main_class = exemple_class()

fr : frame_handler = frame_handler(main_class=main_class, target_fps=60, fps_precision=30, executions_pf=10)

while True:
    fr.basic()
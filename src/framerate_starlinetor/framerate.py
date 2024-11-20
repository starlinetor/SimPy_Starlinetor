import time

class frame_handler :   
    #function                    
    f2execute : function = None #function to be executed by the frame handler
    
    #fps data
    target_fps : int = None                         #fps to achive
    max_spf : float = None                          #max spf aceptable
    executions_pf : int = None                      #executions per frame
    fps_precision: int = None                       #number of terms in calculating the avrage fps and spf
    
    #runtime variables
    start_time : float = 0                          #start time of simulation step
    end_time : float = 0                            #end time of a simulation step
    spf : float = 0                                 #seconds per frame
    
    fps_avrage : list[int] = None                 #these lists store the recorded fps and sfp to output an avrage
    spf_avrage : list[float] = None
    
    def __init__(
        self,
        f2execute : function = print("Executing Function"),
        target_fps : int = 60,
        executions_pf : int = 60,
        fps_precision : int = 60,
        ) -> None:
        """
        Initialize the frame_handler object
        """
        #function
        self.f2execute = f2execute
        #fps data
        self.target_fps = target_fps
        self.max_spf = 1/target_fps
        self.executions_pf = executions_pf
        self.fps_precision = fps_precision 
        
        self.fps_avrage = [(target_fps) for _ in range(fps_precision)]
        self.spf_avrage = [(self.max_spf) for _ in range(fps_precision)]

    def update_fps_spf_avrage (self) -> None:
        #only if there is any actual difference in time we save it
        if(self.end_time - self.start_time != 0):
            self.spf = self.end_time - self.start_time
        #update fps    
        self.fps_avrage.pop(0)
        self.fps_avrage.append(int(1/self.spf))
        #update spf
        self.spf_avrage.pop(0)
        self.spf_avrage.append(self.spf)

    def execute_frame_loose(self, *params, **keyword_params)->None:
        """
        This function will execute loosly the f2execute around the parameters given in the initialize function of the frame_handler.
        This means that it will just execute it {executions_pf} and sleep for the remaining time if there is any left.
        Should be faster to execute and is ideal if you are sure that function is fast enought to execute {executions_pf} times in {max_spf} seconds.
        If you need an adaptive framerate use another function.
        
        Arguments:
            the parameters for the f2execute function
        """
        
        frame_handler.update_fps_spf_avrage(self)
        
        #saves starting time
        self.start_time = time.time_ns() / (10 ** 9)
        
        #renders a frame only every {step_pf} times
        for _ in range(self.step_pf):
            self.f2execute(*params, **keyword_params)
        
        #saves ending time of the frame
        self.end_time  = time.time_ns() / (10 ** 9)
        
        #leftover time is spent sleeping
        if((self.max_spf) - self.end_time + self.start_time >=  0) :
            time.sleep((self.max_spf) - self.end_time + self.start_time)
        
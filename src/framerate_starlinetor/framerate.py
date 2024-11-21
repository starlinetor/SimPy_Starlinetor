import time

class default:
    
    def start(self):
        print("Starting stuff")
    
    def loop(self):
        print("Doing stuff")
    
    def end(self):
        print("Done doing stuff")

class frame_handler :   
    #main class              
    main_class = None                               #This is the main class instance that the frame_handler will reference
    
    #fps data
    target_fps : int = None                         #fps to achive
    max_spf : float = None                          #max spf aceptable
    executions_pf : int = None                      #executions per frame
    fps_precision: int = None                       #number of terms in calculating the average fps and spf
    
    #runtime variables
    start_time : float = 0                          #start time of a frame
    end_time : float = 0                            #end time of a frame
    true_end_time : float = 0                       #true end time of a frame, this counts also the sleep time
    
    fps_average : list[int] = None                 #these lists store the recorded fps and sfp to output an average
    spf_average : list[float] = None
    
    def __init__(
        self,
        main_class = default(),
        target_fps : int = 60,
        executions_pf : int = 60,
        fps_precision : int = 60,
        ) -> None:
        """
        Initialize the frame_handler object
        
        ### Arguments 
        1. main_class : class 
            - instance of the class that handles all the code. It must contain a main() function. Then main function is the one that will be executed repeatedly
        2. target_fps : int
            - the target fps you want to achive
        3. executions_pf : int
            - the number of times the main() function is run]
        4. fps_precision : int
            - how precise you want the average fps and spf calculation to be. Lower values update faster but are less readble
        """
        #function
        self.main_class = main_class
        #fps data
        self.target_fps = target_fps
        self.max_spf = 1/target_fps
        self.executions_pf = executions_pf
        self.fps_precision = fps_precision 
        
        self.fps_average = [(target_fps) for _ in range(fps_precision)]
        self.spf_average = [(self.max_spf) for _ in range(fps_precision)]

    def update_fps_spf_average (self) -> None:
        #remove oldest spf 
        self.spf_average.pop(0)
        #add newest
        self.spf_average.append(self.end_time - self.start_time)

        #remove oldest fps    
        self.fps_average.pop(0)
        #add newest
        if (self.true_end_time - self.start_time != 0):
            self.fps_average.append(int(1/(self.true_end_time - self.start_time)))
        else :
            self.fps_average.append(self.target_fps)
        #update spf
        
    def average_fps (self) -> float : 
        """
        Returns the avrage fps as a float
        """
        return sum(self.fps_average)/len(self.fps_average)
    
    def average_spf (self) -> float : 
        """
        Returns the avrage spf as a float
        """
        return sum(self.spf_average)/len(self.spf_average)

    def execute_frame(self)->None:
        """
        Function that executes the main_class
        """
        
        
        #executes the start function
        self.main_class.start()
        
        #executes the main loop {executions_pf times}
        for _ in range(self.executions_pf):
            self.main_class.loop()
        
        #executes the end function
        self.main_class.end()

    def basic(self)->None:
        """
        The most basic frame_render system meaning no adaptive fps 
        """
        
        frame_handler.update_fps_spf_average(self)
        
        #saves starting time
        self.start_time = time.time_ns() / (10 ** 9)
        
        self.execute_frame()
        
        #saves ending time of the frame
        #this is used to know much to sleep for and to calculate the correct spf
        self.end_time  = time.time_ns() / (10 ** 9)
        
        #leftover time is spent sleeping
        if(self.max_spf - (self.end_time - self.start_time) >=  0) :
            time.sleep(self.max_spf - (self.end_time - self.start_time))
            
        #saves the true ending time of the frame
        #this is used to calculate the correct fps
        self.true_end_time  = time.time_ns() / (10 ** 9)    
        
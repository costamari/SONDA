import numpy as np
import random

class Call:

    def __init__(self, n_nodes, Lambda1, Lambda2):
        
        """
        :param n_nodes: number of nodes
        :param Lambda1: average call arrival rate according to a poissonian process
        :param bit_rate: average call duration rate according to a exponential process
        """
        
        self.n_nodes = n_nodes
        self.Lambda1 = Lambda1
        self.Lambda2 = Lambda2
     
    def Src(self):            
        nodes = range(1, self.n_nodes+1, 1)        
        self.src_node = nodes[random.randint(0,(len(nodes)-1))]        # Randomly assign src node from list
        return self.src_node

    def Dst(self):    
        nodes = range(1, self.n_nodes+1, 1) 
        self.dst_node = nodes[random.randint(0,(len(nodes)-1))]
        while(self.dst_node == self.src_node):                         # Ensure dst node is not equal to source
            self.dst_node = nodes[random.randint(1,(len(nodes)-1))]    # Randomly assign dest node from list         
        return self.dst_node
       
    def BitRate(self):    
        self.bit_rate = random.randint(10,500)                         # Randomly assign bit rate
        return self.bit_rate

    def ArrivalTime(self):          
        # Routine to determine the arrival time of the call
        self.arrival_time = np.random.poisson(self.Lambda1)             
        while (self.arrival_time == 0):                            
            self.arrival_time = np.random.poisson(self.Lambda1)         
        # End of Routine
        return self.arrival_time

    def DurationTime(self):    
        # Routine to determine the duration time of the call
        self.duration_time = np.random.poisson(self.Lambda2)             
        while (self.duration_time == 0):                            
            self.duration_time = np.random.poisson(self.Lambda2)         
        # End of Routine     
        return self.duration_time

    def TrafficLoad(self):    
        return print(self.Lambda1*self.Lambda2)   
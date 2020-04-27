import random

class Call:

    def __init__(self, n_nodes, H, mu):
        
        """
        :param n_nodes: number of nodes
        :param H: t parameter for the cl interarrival time exponential distribution
        :param mu: parameter for the call duration exponential distribution
        """
        
        self.n_nodes = n_nodes
        self.H = H
        self.mu = mu
     
    def Src(self):
        nodes = range(1, self.n_nodes+1, 1)        
        self.src_node = nodes[random.randint(0,(len(nodes)-1))]        # Randomly assign src node from list
        return self.src_node

    def Dst(self):
        nodes = range(1, self.n_nodes+1, 1)  
        self.dst_node = nodes[random.randint(0,(len(nodes)-1))]
        while(self.dst_node == self.src_node):                         # Ensure dst node is not equal to source
            self.dst_node = nodes[random.randint(0,(len(nodes)-1))]    # Randomly assign dest node from list         
        return self.dst_node
       
    def BitRate(self):
        self.bit_rate = random.randint(10,500)                         # Randomly assign bit rate
        return self.bit_rate 

    def ArrivalTime(self):
        self.arrival_time = random.expovariate(self.H)                 # Randomly assign arrival time
        while (self.arrival_time == 0):  
            self.arrival_time = random.expovariate(self.H) 
        return self.arrival_time

    def DurationTime(self):
        self.duration_time = random.expovariate(1/self.mu)             # Randomly assign duration time
        while (self.duration_time == 0):  
            self.duration_time = random.expovariate(1/self.mu)  
        return self.duration_time

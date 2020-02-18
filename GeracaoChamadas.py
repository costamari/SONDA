class Call:

    def __init__(self, src_node, dst_node, bit_rate):

        """
        :param src_node: nó fonte
        :param dst_node: nó destino
        :param bit_rate: taxa de transmissão de bit
        """
        
        self.src_node = src_node    
        self.dst_node = dst_node 
        self.bit_rate = bit_rate

    # --------------- Source and Destination ------------------
    # Get the source and destination nodes and return          
    def GetSrc(self):
        return self.src_node
        
    def GetDst(self):
        return self.dst_node    
        
    # --------------- Bit rate ------------------
    # Get the bit rate em Gbps and return            
    def GetBitRate(self):
        return self.bit_rate          


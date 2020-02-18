class Signal:

    def __init__(self, launch_power, noise_power, modulation_format):

        """
	    :param launch_power: launch power in dBm - float
	    :param noise_power: noise power in dBm - float
        :param modulation_format: modulation format name - string
        """

        self.launch_power = launch_power
        self.noise_power = noise_power
        self.modulation_format = modulation_format

    # --------------- Launch Power ------------------
    # Get the launch power and return      
    def GetLaunchPower(self):    
        return self.launch_power

    # --------------- Noise Power ------------------
    # Get the noise power and return  
    def GetNoisePower(self):    
        return self.noise_power    

    # --------------- Modulation Format ------------------
    # Get the modulation format and return  
    def GetModulationFormat(self):    
        return self.modulation_format    
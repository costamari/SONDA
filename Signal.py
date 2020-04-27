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
   
    def GetLaunchPower(self):    
        return self.launch_power

    def GetNoisePower(self):    
        return self.noise_power    
 
    def GetModulationFormat(self):    
        return self.modulation_format    

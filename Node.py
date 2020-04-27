class Node:

    def __init__(self, label, node_architecture, node_type):

        """
        :param label: node name
        :param node_architecture: node architecture
	:param node_type: node type
        """
        
        self.node_id = id(self)
        self.label = label
        self.node_architecture = node_architecture
        self.node_type = node_type
    
    def GetArchitecture(self):    
        return self.node_architecture

    def GetType(self):    
        return self.node_type

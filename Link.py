from collections import namedtuple

class Link: #https://github.com/adiazmont/optical-network-simulator/blob/master/link.py

    def __init__(self, src_node, dst_node, bidirection=False):
        """
        :param src_node: Node() object
        :param dst_node: Node() object
        """
        if src_node == dst_node:
            raise ValueError("link.__init__ src_node must be different from dst_node!")
        self.link_id = id(self)
        self.src_node = src_node
        self.dst_node = dst_node
        self.bidirection = bidirection

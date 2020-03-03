"""
    algorithm: dijkstra
    1 - mark all nodes unvisited and store them.
    2 - Set the distance to zero for our initial node and to infinity for other neighbors.
    3 - Select the unvisited node with the smallest distance, it's current node now.
    4 - Find unvisited neighbors for the current node and calculate their distances through the current node.
    5 - Compare the newly calculated distance to the assigned and save the smaller one.
    6 - Mark the current node as visited and remove it from the unvisited nodes.
    7 - Stop, if the destination node has been visited.
    8 - If not, loop on step 3.

"""
from collections import defaultdict
from typing import Set, Any


class Dijkstra:

    def __init__(self, nodes, neighbors, distances):
        self.nodes = node
        self.neighbors = defaultdict(list)                      #the argument list indicates that the values will be list type
        self.distances = distances

    def add_node(self, cost):
        self.nodes.add(cost)

    def add_neighbors(self, from_node, to_node, distance):
        self.neighbors[from_node].append(to_node)               #adds a single item to the existing list
        self.neighbors[to_node].append(from_node)               #adds a single item to the existing list
        self.distances[(from_node, to_node)] = distance         #the distance will be determinated by the cost between the current node and the neighbour

    def dijsktra(self, current_node):
        visited = {current_node: 0}                             #the initial cost for the current node following the dijkstra algorithm is 0

        nodes = set(graph.nodes)

        while nodes:
            min_node = None
            node: object
            for node in nodes:                                  #for node in nodes makes a test descripted in the algorithm steps 3-6
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if visited[node] == visited[min_node]:              #stop if the destination node has been visited.
                break
"""
    algorithm: dijkstra
    1 - mark all nodes unvisited and store them.
    2 - Set the distance to zero for our initial node and to infinity for other neighbors.
    3 - Select the unvisited node with the smallest distance, it's current node now.
    4 - Find unvisited neighbors for the current node and calculate their distances through the current node.
    5 - Compare the newly calculated distance to the assigned and save the smaller one.
    6 - Mark the current node as visited and remove it from the unvisited nodes.
    7 - Stop, if the destination node has been visited or if the smallest distance among the unvisited nodes is infinity.
    8 - If not, loop on step 3.

"""
from collections import defaultdict

#initially all the costs are infinite
inf = float('inf')

class Dijkstra:

    def __init__(self, node, neighbors, distance):
        self.node = node
        self.neighbors = defaultdict(list)  # the argument list indicates that the values will be list type
        self.distance = distance

    def add_node(self, cost):  # for the node we add the cost of each route
        self.node.add(cost)

    def add_neighbors(self, from_node, to_node, distance):
        self.neighbors[from_node].append(to_node)  # adds a single item to the existing list
        self.neighbors[to_node].append(from_node)  # adds a single item to the existing list
        self.distance[(from_node,
                       to_node)] = distance  # the distance will be determinated by the cost between the current node and the neighbour
        self.distance[(to_node, from_node)] = distance

    def dijsktra(self, current_node):
        visited = {current_node: 0}  # the initial cost for the current node following the dijkstra algorithm is 0
        path = set()  # this function returns the chosen path with the less cost

        nodes = set(self.node)

        while nodes:
            initial_node = None  # The None keyword is used to define a null variable or an object
            for node in nodes:
                if node in visited:
                    if initial_node is None:
                        initial_node = node
                    elif visited[node] < visited[initial_node]:
                        initial_node = node

            if visited[node] == visited[initial_node] or current_cost == inf: # step 7
                print('Bloqueio')
                break

            nodes.remove(initial_node)
            current_cost = visited[initial_node]

            for neighbors in self.neighbors[initial_node]:
                current_cost = current_cost + self.distance[(initial_node,
                                                             neighbors)]  # the current cost is given by: current cost + the cost from the distance between the node and the neighbor
                if neighbors not in visited or current_cost < visited[neighbors]:
                    visited[neighbors] = current_cost
                    path[neighbors] = initial_node

        return visited, path # returns the path and the visited nodes

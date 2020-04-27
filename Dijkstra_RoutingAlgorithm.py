import networkx as nx

def Dijkstra(A, src_node, dst_node):
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    path = nx.dijkstra_path(G, src_node, dst_node)
    return path

def ShortestDistance(A, src_node, dst_node):
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    distance = nx.shortest_path_length(G, src_node, dst_node)
    return distance 

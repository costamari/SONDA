import networkx as nx

def dijkstra(A, src, dst):
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    print('The shortest path acording to dijkstra algorithm is:', nx.dijkstra_path(G, src, dst))  
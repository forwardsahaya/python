import numpy as np
def create_adjacency_matrix(num_vertices):
    return np.zeros((num_vertices, num_vertices), dtype=int )
#Example usage
graph = create_adjacency_matrix(4)
graph[0, 1] = 1
#Add  an edge from vertex 0 to vertex 1
graph[1, 0] = 1
#Add an edge from vertex 1 to vertex 0

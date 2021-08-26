
from math import inf 
from heapq import heappush, heappop 

def dijkstras(graph, start):
    distances = {}
    for vertex in graph.keys():
        distances[vertex] = inf 
    distances[start] = 0 

    vertices_to_explore = [(0, start)]
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbour, weight in graph[current_vertex]:
            if weight < 0:
                weight = abs(weight)
            new_distance = current_distance + weight 

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance 
                heappush(vertices_to_explore, (new_distance, neighbour))
    
    return distances 



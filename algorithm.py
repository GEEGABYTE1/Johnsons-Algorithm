from dijkstras import dijkstras
from graph import graph 

def johnsons(graph):
    graph_edges = {}
    for vertex, lst in graph.items():
        new_lst = []
        for tuple in lst:
            edge = tuple[0]
            new_lst.append(edge)
        graph_edges[vertex] = new_lst
    
    graph_vertices = graph_keys(graph)
    dijkstras_returns = []
    
    for vertex in graph_vertices:
        dijkstra_return = dijkstras(graph, vertex)
        dijkstras_returns.append(dijkstra_return)
    
    
    shortest_distances = {}
 

    for vertex in range(len(graph_vertices)):
        dictionary = {}
        right_pointer = -1
        while right_pointer != len(dijkstras_returns) * -1:
            current_dijkstra = dijkstras_returns[vertex]
            root_elm = graph_vertices[vertex]
            last_dijkstra = dijkstras_returns[right_pointer]
            head_last = graph_vertices[right_pointer]
            current_dijkstra_val = current_dijkstra.get(head_last)
            last_dijkstra_val = last_dijkstra.get(root_elm)
            if current_dijkstra_val < last_dijkstra_val:
                dictioanry[root_elm] = [current_dijkstra_val, head_lst]
            else:
                dictionary[head_last] = [last_dijkstra_val, root_elm]

            right_pointer -= 1
    
        shortest_distances[graph_vertices[vertex]] = dictionary
    
    return shortest_distances


def graph_keys(graph):
    graph_vertices = list(graph.keys())
    return graph_vertices


print(johnsons(graph))
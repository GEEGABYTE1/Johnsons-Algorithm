from vertex import Vertex 

class Graph:
    def __init__(self, directed=False):
        self.directed = directed 
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex 

    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)

        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop()
            print(current_vertex)
            seen[current_vertex] = True 
            if current_vertex == end_vertex:
                return True 
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [i for i in next_vertices if not i in seen]
                start.extend(next_vertices)
    
        return False 


test = Graph()

one = Vertex(1)
two = Vertex(2)
three = Vertex(3)
four = Vertex(4)
five = Vertex(5)

test.add_vertex(one)
test.add_vertex(two)
test.add_vertex(three)
test.add_vertex(four)
test.add_vertex(five)

test.add_edge(one, two, 1)
test.add_edge(two, three, 4) 
test.add_edge(three, one, -2)
test.add_edge(three, four, 8)
test.add_edge(four, two, 6)
test.add_edge(four, five, 5)



# Dijkstras Input 

graph = {}

for vertex, neighbour in test.graph_dict.items():
    lst = []
    edges = neighbour.edges 
    for secondary_neighbour, weight in edges.items():
        lst.append((secondary_neighbour, weight))
    graph[vertex] = lst 


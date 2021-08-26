# Johnsons Algorithm 🔎

Re-creation Johnson's Algorithm in my own way. 

The Algorithm is used to find the shortest paths between every pair of vertices in a given weighted directed Graph, where weights may be negative.

# Solution 🔮

As you can see, this algorithm sort of relates to Dijkstras and the Floyd Warshall Algorithm. Therefore, we can use Dijsktras for our solution, however, 
since Dijkstras can only compute positive edges, we will use the idea of Johnson's Alogrithm where we re-weight all the edges andd make them all positive. In order
to this, we add a number to the negative edge to make equivalent to 0. For the rest of the edges, we add the same number in order to keep the "negative edge" the 
smallest edge. We have two cases to increase the negative edge and still keeps it "smallest edge" identity:
 - 1) If our summation factor (a factor of which we increase all the edges) is equivalent to 0, then the first edge that is negative will then be the summation factor.
 - 2) If the summation factor is smaller than the absolute value of the current weight, then the absolute difference between them will be added to the summation factor.

While formatting the graph into a dictionary (see *More Information* on how I have formatted the graph), we increase each edge by the summation factor.

After that, we compute the dijkstras algorithm on every vertex and store it in a list for reference. By definition, we know that the dijkstras algorithm will compute the 
shortest edge in order of when each vertex had been added to the vertex. For example, if `1, 2, 3, 4, 5` were added to the graph, then the dijkstras would compute the edges of each vertex
in order of `[1, 2, 3, 4, 5]`. 

Thus, by understanding that each index of the keys in the graph (since we have formatted the graph into a dictionary) is equivalent to the index of the lists of dijkstras 
computed edges, vertex by vertex, we compare each distance by integrating a for loop and a semi pointer to keep track of the dijkstras computed values from different vertices. We
compare each edge of the "root vertex" to the edges of the pointer, and we see if it is lower, greater, or the same. Based on that, we add it to the dictionary, and after all the vertices have been compared 
with the current vertex, we add it to our returned dictionary (which is different then the dictionary to keep compared edges). To traverse the list of dijkstras values while comparing, we increase subtract the pointer by one 
to continue to the traversal in order to compare each vertex's edges. This allows for a comparision of all vertices for each current vertex in the for loop. 

Time Complexity: `O(V^2 log V + VE)`

# More Information 📕
`algorithm.py` is our algorithm. Note that `.graph_keys()` is a helper function to reference the graph's vertices. 
`dijkstras.py` is the Dijkstras Algorithm 
`graph.py` is our underlying graph data structure. At the bottom, I have formatted the dictionary: `{vertex: [(neighbour, weight), (neighbour2, weight2)]...}`, which is used for the Johnson's Algorithm. As well, this is where we compute negative edges.
`vertex.py` is to reference and create Vertex objects for the graph.

Made in Python 🐍



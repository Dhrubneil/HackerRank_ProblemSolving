from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, source):
        visited = [False] * (len(self.graph))

        queue = []

        queue.append(source)
        visited[source] = True
        print(visited)
        while queue:
            vertex = queue.pop(0)

            print(vertex, end=" ")

            for adj_node in self.graph[vertex]:
                if visited[adj_node] == False:
                    queue.append(adj_node)
                    visited[adj_node] = True
    
my_graph = Graph()
my_graph.addEdge(0,1)
my_graph.addEdge(0,2)
my_graph.addEdge(1,2)
my_graph.addEdge(2,0)
my_graph.addEdge(2,3)
my_graph.addEdge(3,3)

my_graph.BFS(2)

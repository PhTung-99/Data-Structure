all_edge = [("A", "B"), ("A","C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'

    def add_neighbors(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
        
class Graph:
    vertexs = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertexs:
            self.vertexs[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertexs and v in self.vertexs:
            for key, value in self.vertexs.items():
                if key == u:
                    value.add_neighbors(v)
                if key == v:
                    value.add_neighbors(u)
            return True
        return False

    def printGraph(self):
        for key in sorted(list(self.vertexs.keys())):
            print(key + ": " + str(self.vertexs[key].neighbors) + " " 
                + str(self.vertexs[key].distance) + " " + str(self.vertexs[key].color))
             

graph = Graph()
a = Vertex('A')
graph.add_vertex(a)
graph.add_vertex(Vertex("B"))
for i in range(ord('A'), ord('K')):
    graph.add_vertex(Vertex(chr(i)))

edges = ["AB", 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FE', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.add_edge(edge[1:], edge[:1])

graph.printGraph()
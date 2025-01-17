import networkx as nx

class DirectedGraph:
    """Graph representation using adjacency list"""    

    def __init__(self, vertices: int):
        """Initializes graph object with given number of vertices"""
        self.vertices = vertices
        self.adjacency = [[] for _ in range(vertices)]

    def add_edge(self, vertex1: int, vertex2: int):
        """Adds edge directed from vertex1 to vertex2"""
        self.adjacency[vertex1].append(vertex2)

    def to_nx_graph(self) -> nx.DiGraph:
        """Returns nx.DiGraph object for visualization purpurose"""
        digraph = nx.DiGraph()
        for vertex, neighbors in enumerate(self.adjacency):
            for neighbor in neighbors:
                digraph.add_edge(vertex, neighbor)
        return digraph
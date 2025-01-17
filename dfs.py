from typing import List
from graph import DirectedGraph
import matplotlib.pyplot as plt
import networkx as nx
import time

class DFS:
    def __init__(self, graph: DirectedGraph) -> None:
        self.graph: DirectedGraph = graph
        self.visited: List[bool] = [False] * graph.vertices
        self.rec_stack: List[bool] = [False] * graph.vertices
        self.order: List[int] = []
        self.has_cycle: bool = False

    def _dfs_recursion(self, vertex: int) -> None:
        """Helper method for recursion"""
        self.visited[vertex] = True
        self.rec_stack[vertex] = True
        self.order.append(vertex)

        for neighbor in self.graph.adjacency[vertex]:
            if not self.visited[neighbor]:
                self._dfs_recursion(neighbor)
            elif self.rec_stack[neighbor]:
                self.has_cycle = True
        
        self.rec_stack[vertex] = False

    def dfs_traverse(self, start_vertex: int) -> List[int]:
        """Performs recursive DFS algorithm in a directed graph"""
        self._dfs_recursion(start_vertex)
        return self.order

    def visualize_search(self) -> None:
        """Visualizes the DFS traversal"""
        graph = self.graph.to_nx_graph()
        pos = nx.spring_layout(graph)
        visited_nodes = set()

        plt.figure()
        plt.title("DFS visualization in directed graph")
        for i, node in enumerate(self.order, start=1):
            plt.clf()
            visited_nodes.add(node)
            plt.title("DFS visualization in directed graph")
            nx.draw(graph,
                    pos,
                    with_labels=True,
                    node_color=['r' if n == node else 'grey' if n in visited_nodes else 'g' for n in graph.nodes])
            plt.draw()
            plt.pause(1)
        plt.show()
        time.sleep(0.5)

if __name__ == "__main__":
    g = DirectedGraph(10)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 7)
    g.add_edge(4, 7)
    g.add_edge(5, 8)
    g.add_edge(6, 8)
    g.add_edge(7, 9)
    g.add_edge(8, 9)

    dfs = DFS(g)
    dfs.dfs_traverse(0)
    dfs.visualize_search()

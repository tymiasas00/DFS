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
        
        def on_close(event):
            plt.close('all')

        fig = plt.figure()
        fig.canvas.mpl_connect('close_event', on_close)
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

    

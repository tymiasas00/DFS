import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

order = []

def add_edge(adj, vertex1, vertex2):
    # Add edge from vertex s to t
    adj[vertex1].append(vertex2)

def dfs_recursion(adj, visited, vertex):
    # Mark the current vertex as visited
    visited[vertex] = True
    order.append(vertex)

    # Print the current vertex
    print(vertex, end=" ")

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[vertex]:
        if not visited[i]:
            dfs_recursion(adj, visited, i)

def dfs(adj, start_vertex):
    visited = [False] * len(adj)
    # Call the recursive DFS function
    dfs_recursion(adj, visited, start_vertex)
    return order


def animate_dfs(adj, visited_order):
    G = nx.DiGraph()
    for u in range(len(adj)):
        for v in adj[u]:
            G.add_edge(u, v)

    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)
    # Make every node the same color at the beginning
    color_map = ['lightblue'] * len(adj)

    def update(frame):
        node = visited_order[frame]
        color_map[node] = plt.cm.viridis(frame / max(1, len(visited_order) - 1))
        ax.clear()
        nx.draw(
            G,
            pos=pos,
            with_labels=True,
            node_color=color_map,
            edge_color='gray',
            arrowsize=15,
            arrowstyle='->',
            ax=ax
        )

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(visited_order),
        interval=1000,
        repeat=False
    )
    plt.show()

if __name__ == "__main__":
    V = 5

    adj = [[] for _ in range(V)]

    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]]

    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 0
    print("DFS from source:", source)
    visited_order = dfs(adj, source)
    animate_dfs(adj, visited_order)
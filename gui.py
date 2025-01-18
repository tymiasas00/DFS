import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph import DirectedGraph
from dfs import DFS  # Assuming your DFS class is in a file named dfs.py
import json

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("DFS Visualization GUI")
        self.filename = None
        self.loaded_graphs = {}  # dictionary to store loaded graphs

        # Frame for Buttons
        self.frame = ttk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Visualize Button
        self.visualize_button = ttk.Button(self.frame, text="Visualize DFS", command=self.visualize_search)
        self.visualize_button.pack(side=tk.TOP, pady=10)

        # Load json Button
        self.load_json_button = ttk.Button(self.frame, text="Load Graphs from json", command=self.select_json_file)
        self.load_json_button.pack()

        # Listbox for loaded graphs
        self.loaded_graph_list = tk.Listbox()
        self.loaded_graph_list.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Starting Node Entry
        self.start_node_label = ttk.Label(self.frame, text="Start Node:")
        self.start_node_label.pack(side=tk.TOP, pady=5)
        self.start_node_entry = ttk.Entry(self.frame)
        self.start_node_entry.pack(side=tk.TOP, pady=5)
    
    def select_json_file(self) -> None:
        """Opens file dialog to load"""
        filetypes = (
            ('JSON', "*.json"),
            ('All files', '*.*')
        )

        self.filename = fd.askopenfilename(
            title='Select json file containing adjacency lists', 
            filetypes=filetypes
        )
        if self.filename:
            self.load_graphs_from_json(self.filename)
        

    def load_graphs_from_json(self, filename) -> None:
        """Loads graphs from a JSON file and populates the Listbox with graph names."""
        with open(filename, 'r') as file:
            graphs = json.load(file)
            self.loaded_graph_list.delete(0, tk.END)  # Clear the Listbox
            for graph_name, adjacency_list in graphs.items():
                self.loaded_graph_list.insert(tk.END, graph_name)
                self.loaded_graphs[graph_name] = adjacency_list
    
    def display_cycle_message(self) -> None:
        """Displays a message box indicating the presence of a cycle."""
        tk.messagebox.showinfo("Cycle Detected", "The graph has a cycle.")

    def display_incorrect_node_message(self) -> None:
        """Displays a message box indicating an incorrect node."""
        tk.messagebox.showinfo("Incorrect Node", "The start node is not in the graph.")
    

    def visualize_search(self) -> None:
        """Visualizes DFS on the selected graph."""
        selection = self.loaded_graph_list.curselection()
        if not selection:
            print("No graph selected")
            return
        selected_graph_name = self.loaded_graph_list.get(selection)
        print(f"Selected graph: {selected_graph_name}")

        adjacency_list = self.loaded_graphs[selected_graph_name]
        print(f"Adjacency list: {adjacency_list}")

        # Create a DirectedGraph from the adjacency list
        max_node = max(max(edge) for edge in adjacency_list)
        g = DirectedGraph(max_node + 1)
        for edge in adjacency_list:
            g.add_edge(edge[0], edge[1])

        # Get the starting node from the entry
        start_node = int(self.start_node_entry.get())
        if start_node < 0 or start_node > max_node:
            self.display_incorrect_node_message()
            return

        # Set the graph for DFS and visualize
        dfs = DFS(g)
        dfs.dfs_traverse(start_node)
        if dfs.has_cycle:
            self.display_cycle_message()
        dfs.visualize_search()


if __name__ == "__main__":
    

    root = tk.Tk()
    app = App(root)
    root.mainloop()

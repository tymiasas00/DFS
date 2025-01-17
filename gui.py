import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Directed Graph DFS Visualizer")

        # Left Frame
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

        # Listbox for graphs
        self.graph_listbox = tk.Listbox(self.left_frame, width=30, height=15)
        self.graph_listbox.pack(pady=5)

        # Buttons
        self.load_button = tk.Button(self.left_frame, text="Load Graphs", command=None)
        self.load_button.pack(pady=5)

        self.visualize_button = tk.Button(self.left_frame, text="Run Visualization", command=None) # TODO : Implement visualization from dfs class
        self.visualize_button.pack(pady=5)

        # Right Frame
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Placeholder for graphs
        self.graphs = {}

     


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphVisualizer(root)
    root.mainloop()

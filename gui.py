import tkinter as tk
from tkinter import ttk
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter OOP Example")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.placeholder_frame = ttk.Entry(self, background="lightblue")
        self.placeholder_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.button1 = ttk.Button(self, text="Load CSV", command=self.load_csv)
        self.button1.grid(row=1, column=0, padx=(10, 2), pady=10, sticky="w")

        self.button2 = ttk.Button(self, text="Generate adjucency\n matrix", command=self.generate_adjucency_matrix)
        self.button2.grid(row=1, column=1, padx=(2, 10), pady=10, sticky="w")

    def load_csv(self):
        self.placeholder_frame.delete(0, tk.END)
        self.placeholder_frame.insert(0, "Loading CSV...")
        self.update()
        time.sleep(1)
        self.placeholder_frame.insert(0, "CSV Loaded")

    def generate_adjucency_matrix(self):
        matrix_window = tk.Toplevel(self)
        matrix_window.title("Adjacency Matrix")

        size_label = ttk.Label(matrix_window, text="Enter matrix size:")
        size_label.pack(pady=10)

        size_entry = ttk.Entry(matrix_window)
        size_entry.pack(pady=5)

        def create_matrix():
            try:
                size = int(size_entry.get())
                for widget in matrix_window.winfo_children():
                    widget.destroy()

                for i in range(size):
                    # Create column headers
                    col_label = ttk.Label(matrix_window, text=str(i+1))
                    col_label.grid(row=0, column=i+1, padx=5, pady=5)

                    # Create row headers
                    row_label = ttk.Label(matrix_window, text=str(i+1))
                    row_label.grid(row=i+1, column=0, padx=5, pady=5)

                    for j in range(size):
                        var = tk.IntVar()
                        chk = tk.Checkbutton(matrix_window, variable=var)
                        chk.grid(row=i+1, column=j+1)
            except ValueError:
                error_label = ttk.Label(matrix_window, text="Please enter a valid number")
                error_label.pack(pady=10)

        create_button = ttk.Button(matrix_window, text="Create Matrix", command=create_matrix)
        create_button.pack(pady=10)

    def on_button_click(self):
        print("Button Clicked!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('DFS Visualizer')
        self.geometry('400x300')
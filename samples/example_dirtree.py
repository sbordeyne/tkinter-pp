import tkinter as tk
import tkinterpp
import os


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.dirtree = tkinterpp.DirTree(self, os.getcwd())
        self.dirtree.populate_roots()
        self.dirtree.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("DirTree Example")
    gui = MainWindow(root)
    gui.pack()
    root.mainloop()

import tkinter as tk
from tkinterpp import DraggableNotebook


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.nb = DraggableNotebook(self)
        self.nb.add(tk.Canvas(self.nb, width=400, height=300), text="canv1")
        self.nb.add(tk.Canvas(self.nb, width=400, height=300), text="canv2")
        self.nb.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Draggable Notebook Example")
    gui = MainWindow(root)
    gui.pack()
    root.mainloop()

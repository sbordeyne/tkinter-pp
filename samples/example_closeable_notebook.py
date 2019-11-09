import tkinter as tk
import tkinterpp


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.notebook = tkinterpp.CloseableNotebook(self)
        for i in range(3):
            text = tkinterpp.TextWithLineNumbers(self.notebook)
            self.notebook.add(text, text=f"Tab {i}")
        self.notebook.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Closeable Notebook Example")
    gui = MainWindow(root)
    gui.pack()
    root.mainloop()
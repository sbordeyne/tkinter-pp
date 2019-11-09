import tkinter as tk
import tkinterpp


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.text = tkinterpp.TextWithLineNumbers(self)
        self.text.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Text With Line Numbers Example")
    gui = MainWindow(root)
    gui.pack()
    root.mainloop()
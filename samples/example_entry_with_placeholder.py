import tkinter as tk
import tkinterpp


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entry = tkinterpp.EntryWithPlaceholder(self, placeholder="An Example of placeholder", width=80)
        self.entry1 = tkinterpp.EntryWithPlaceholder(self, placeholder="An Example of placeholder", width=80)
        self.entry.pack()
        self.entry1.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Example of entry with placeholder")
    gui = MainWindow(root)
    gui.pack()
    root.mainloop()

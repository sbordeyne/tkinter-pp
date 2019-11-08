import tkinter as tk
import tkinterpp


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.date = tkinterpp.variables.DateVar()
        self.calendar = tkinterpp.Calendar(self, variable=self.date)
        self.calendar.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calendar Example")
    gui = MainWindow(root)
    gui.pack()
    root.mainloop()

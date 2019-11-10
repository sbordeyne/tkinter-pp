import tkinter as tk
import tkinterpp


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pos = tk.StringVar()
        self.node_name = tk.StringVar()

        self.node_view = tkinterpp.NodeView(self)
        self.node_view.grid()
        frame = tk.Frame(self)
        tk.Button(frame, text="Add Node", command=self.add_node).grid()
        tkinterpp.EntryWithPlaceholder(frame, textvariable=self.pos, placeholder="POS").grid()
        tkinterpp.EntryWithPlaceholder(frame, textvariable=self.node_name, placeholder="NODE NAME").grid()
        frame.grid(row=1)

    def add_node(self, *args):
        pos = [int(i) for i in self.pos.get().split(" ")]
        self.node_view.create_node(pos, self.node_name.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("NodeView Example")
    gui = MainWindow(root)
    gui.grid()
    root.mainloop()

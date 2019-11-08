import tkinter as tk
import tkinterpp


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.menu = tkinterpp.PopupMenu(self, callbacks=[self.on_context_menu_open])
        self.menu.add_command(label="Foo", command=self.dummy)
        self.menu.add_command(label="Bar", command=self.dummy)
        self.menu.add_command(label="Baz", command=self.dummy)

    @staticmethod
    def on_context_menu_open(event):
        print("Context menu opened!")

    @staticmethod
    def dummy():
        print("Dummy call.")


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x300")
    gui = MainWindow(root)
    gui.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

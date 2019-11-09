import tkinter as tk
import tkinterpp


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        i = 0
        self.bitmaps = []
        for name, bitmap in tkinterpp.Bitmap().dict.items():
            tk.Label(self, text=name).grid(row=i, column=0)
            self.bitmaps.append(bitmap())
            tk.Button(self, image=self.bitmaps[i]).grid(row=i, column=1)
            i += 1


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Assets Example")
    gui = MainWindow(root)
    gui.grid()
    root.mainloop()

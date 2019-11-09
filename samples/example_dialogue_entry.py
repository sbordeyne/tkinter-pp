import tkinter as tk
import tkinterpp


if __name__ == '__main__':
    def open_entry():
        tkinterpp.DialogueEntry()
    root = tk.Tk()
    btn = tk.Button(root, text="open entry toplevel", command=open_entry)
    btn.pack()
    root.mainloop()

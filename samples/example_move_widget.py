import tkinter as tk
from tkinterpp.utils import move_widget


root = tk.Tk()
root.title("root")
tl = tk.Toplevel(root)
tl.title("toplevel")
label = tk.Label(root, text="A LABEL")
label.pack()
print(repr(label))
label = move_widget(label, tl)
print(repr(label))
label.pack()
print(root.winfo_children(), tl.winfo_children())
root.mainloop()

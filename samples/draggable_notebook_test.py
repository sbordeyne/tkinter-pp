import tkinter as tk
import tkinter.ttk as ttk


class DraggableNotebook(ttk.Notebook):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mouse_button_1_pressed = False

        self.bind("<ButtonPress-1>", self._on_mouse_button_1_pressed)
        self.bind("<ButtonRelease-1>", self._on_mouse_button_1_released)
        self.bind("<<NotebookTabChanged>>", self._on_notebook_tab_changed)

    def _on_mouse_button_1_pressed(self, event=None):
        self._mouse_button_1_pressed = (event.x, event.y)

    def _on_mouse_button_1_released(self, event=None):
        self._mouse_button_1_pressed = False

    def _on_notebook_tab_changed(self, event=None):
        if self._mouse_button_1_pressed:
            self.insert(f"@{event.x},{event.y}", self.identify(*self._mouse_button_1_pressed))


root = tk.Tk()
gui = tk.Frame(root)
nb = DraggableNotebook(gui)
canv = tk.Canvas(gui, width=300, height=300)
nb.add(canv, text="canvas1")
canv2 = tk.Canvas(gui, width=300, height=300)
nb.add(canv2, text="canvas2")
canv.pack()
canv2.pack()
nb.pack()
gui.pack()
root.mainloop()

import tkinter as tk
import _tkinter


class PopupMenu(tk.Menu):
    def __init__(self, *args, **kwargs):
        kwargs["tearoff"] = 0
        self.callbacks = kwargs.get("callbacks", [])
        del kwargs["callbacks"]
        super().__init__(*args, **kwargs)
        self.master.bind('<Button-3>', self.display_contextual)

    def display_contextual(self, event):
        for callback in self.callbacks:
            callback(event)
        try:
            self.tk_popup(event.x_root, event.y_root, 0)
        except _tkinter.TclError:
            pass
        finally:
            self.grab_release()

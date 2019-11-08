import tkinter as tk
from . import assets


class Bitmap:
    def __init__(self):
        for name, value in [(n, v) for n, v in assets.__dict__.items() if
                            not n.startswith("__") and not n.endswith("_mask")]:
            self.__dict__[name] = lambda **kwargs: tk.BitmapImage(data=value,
                                                                  maskdata=assets.__dict__[name+"_mask"],
                                                                  **kwargs)


def folder():
    return tk.BitmapImage(data=assets.folder, mask_data=assets.folder_mask)

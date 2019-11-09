import tkinter as tk
from . import assets


class Bitmap:
    """
    The Bitmap class is used to hold all the bitmap generating lambdas, generating from
    the assets in this module.

    Check the assets documentation for a full list of assets.
    """
    def __init__(self):
        for name, value in [(n, v) for n, v in assets.__dict__.items() if
                            not n.startswith("__") and not n.endswith("_mask")]:
            self.__dict__[name] = lambda **kwargs: tk.BitmapImage(data=value,
                                                                  maskdata=assets.__dict__[name+"_mask"],
                                                                  **kwargs)


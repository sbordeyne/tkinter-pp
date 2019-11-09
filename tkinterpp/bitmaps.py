import tkinter as tk
from . import assets


class Bitmap:
    """
    The Bitmap class is used to hold all the bitmap generating lambdas, generating from
    the assets in this module.

    Check the assets documentation for a full list of assets.
    """
    def __init__(self):
        self.dict = {}
        for name in [n for n in assets.__dict__.keys() if
                     not n.startswith("__") and not n.endswith("_mask")]:
            f = lambda n=name, **kwargs: tk.BitmapImage(data=assets.__dict__[n],
                                                        maskdata=assets.__dict__[n+"_mask"],
                                                        **kwargs)
            self.__dict__[name] = f
            self.dict[name] = f

    def __getitem__(self, item):
        if item in self.dict.keys():
            return self.dict[item]
        else:
            raise KeyError(f"No Bitmap matching {item} could be found.")

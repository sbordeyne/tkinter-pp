import tkinter as tk
from . import assets


def folder():
    return tk.BitmapImage(data=assets.folder, mask_data=assets.folder_mask)

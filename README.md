# tkinter-pp
A collection of tkinter made widgets

# Widgets included

## Calendar widget
![Calendar Widget Screenshot](/images/calendar_widget.png)

Displays a calendar so that the user can enter a date.

## CloseableNotebook widget
A subclass of the `ttk.Notebook` widget, with a closing button, so the tab destroys itself.

## ScrolledCanvas widget 
A `tk.Canvas` instance, which has scrollbars built-in to scroll the Canvas in any direction.

## EntryWithPlaceholder
A `tk.Entry` which provides a greyed-out placeholder if nothing is written inside, and unfocused

## KeybindingEntry
A `tk.Entry` which reacts to key presses, so that you can record keybindings in a tkinter-friendly way.

## EntrySelectFolder
A `tk.Entry` which provides a button to select a folder using `tkinter.filedialog.askdirectory`.

The path writes itself inside the entry.

## DialogueEntry
A dialogue box with a `tk.Entry` inside.

## LabelEntry
A label and an entry packaged in one label. You can provide configure options for each of the label
by prefacing the kwarg name with `label_` and `entry_`. You can supply any `Entry` widget, defaulting
to `tk.Entry`.


# Assets included

Some xbm bitmaps are available as well, in a string form. Use `tk.BitmapImage(data=..., mask_data=...)`
to create the bitmaps.

The assets are available in the "assets" submodule. Use `import tkinterpp.assets` to import.

You can also generate a bitmap object directly through the `Bitmap` class in this fashion:
```python
from tkinterpp import Bitmap
bitmap = Bitmap()

folder = bitmap.folder()  # folder bitmap object

folder_yellow = bitmap.folder(fg='yellow')  # yellow folder bitmap object
```

# Create Tooltips

A simple class to add tooltips to any tkinter widget. Simply create an instance of `CreateTooltip`, 
pass in the widget you want the tooltip to appear on, and the text of the tooltip
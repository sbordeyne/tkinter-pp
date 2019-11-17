try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk
from PIL import Image, ImageTk

from .utils import get_root_widget


class ScrolledCanvas(tk.Frame):
    """
    1. Master widget gets scrollbars and a canvas. Scrollbars are connected
    to canvas scrollregion.

    2. self.scrollwindow is created and inserted into canvas

    Usage Guideline:
    Assign any widgets as children of <ScrolledWindow instance>.scrollwindow
    to get them inserted into canvas

    __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs)
    docstring:
    Parent = master of scrolled window
    canv_w - width of canvas
    canv_h - height of canvas

    """

    def __init__(self, parent, canv_w=400, canv_h=400, *args, **kwargs):
        """Parent = master of scrolled window
        canv_w - width of canvas
        canv_h - height of canvas

       """
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        # creating a scrollbars
        self.xscrlbr = ttk.Scrollbar(self.parent, orient='horizontal')
        self.xscrlbr.grid(column=0, row=1, sticky='ew', columnspan=2)
        self.yscrlbr = ttk.Scrollbar(self.parent)
        self.yscrlbr.grid(column=1, row=0, sticky='ns')
        # creating a canvas
        self.canv = tk.Canvas(self.parent)
        self.canv.config(relief='flat',
                         width=canv_w,
                         heigh=canv_h, bd=2)
        # placing a canvas into frame
        self.canv.grid(column=0, row=0, sticky='nsew')
        # accociating scrollbar comands to canvas scroling
        self.xscrlbr.config(command=self.canv.xview)
        self.yscrlbr.config(command=self.canv.yview)

        # creating a frame to inserto to canvas
        self.scrollwindow = ttk.Frame(self.parent)

        self.canv.create_window(0, 0, window=self.scrollwindow, anchor='nw')

        self.canv.config(xscrollcommand=self.xscrlbr.set,
                         yscrollcommand=self.yscrlbr.set,
                         scrollregion=(0, 0, 100, 100))

        self.yscrlbr.lift(self.scrollwindow)
        self.xscrlbr.lift(self.scrollwindow)
        self.scrollwindow.bind('<Configure>', self._configure_window)
        self.scrollwindow.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self._unbound_to_mousewheel)

        return

    def _bound_to_mousewheel(self, event):
        self.canv.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canv.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _configure_window(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
        self.canv.config(scrollregion='0 0 %s %s' % size)
        if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canv.config(width=self.scrollwindow.winfo_reqwidth())
        if self.scrollwindow.winfo_reqheight() != self.canv.winfo_height():
            # update the canvas's width to fit the inner frame
            self.canv.config(height=self.scrollwindow.winfo_reqheight())


class CanvasTransparency(tk.Canvas):
    def __init__(self, **kwargs):
        super(CanvasTransparency, self).__init__(**kwargs)
        self._images = []
        self._tags_ids = {"rectangle": 0,
                          "oval": 0,
                          "polygon": 0}

    def create_rectangle(self, *args, **kwargs):
        """
        Superclass of Canvas.create_rectangle. Creates a rectangle on the canvas, with transparency support.
        Supports all the arguments for the Canvas.create_rectangle method

        :param alpha: float (0.0 <= a <= 1.0) representing the alpha of the filler.
        :return: id of the rectangle
        """
        if len(args) == 1 and isinstance(args[0], (tuple, list)):
            x1, y1, x2, y2 = args[0]
        elif len(args) == 4:
            x1, y1, x2, y2 = args
        else:
            raise ValueError("Incorrect number of arguments passed to function create_rectangle or CanvasTransparency")

        tag = "alpharect{}".format(self._tags_ids["rectangle"])
        self._tags_ids["rectangle"] += 1
        tags = kwargs.get("tags", [])
        tags += ["allaplharects", tag]

        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = get_root_widget(self).winfo_rgb(fill) + (alpha, )
            image = Image.new('RGBA', (x2 - x1, y2 - y1), fill)
            self._images.append(ImageTk.PhotoImage(image))
            self.create_image(x1, y1, image=self._images[-1], anchor='nw', tags=tags)
        super(CanvasTransparency, self).create_rectangle(x1, y1, x2, y2, **kwargs)
        return tag

    def create_oval(self, *args, **kwargs):
        super(CanvasTransparency, self).create_oval(*args, **kwargs)

    def create_polygon(self, *args, **kwargs):
        super(CanvasTransparency, self).create_polygon(*args, **kwargs)

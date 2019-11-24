import tkinter as tk
import tkinter.ttk as ttk
import _tkinter


class CloseableNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, *args, side="left", **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CloseableNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)
        self._active = None
        self.side = side
        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']):
            return

        element = self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if "close" in element and self._active == index:
            self.forget(index)
            if self.side == "left":
                self.master.left_tabs.pop(index)
            else:
                self.master.right_tabs.pop(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )
        try:
            style.element_create("close", "image", "img_close",
                                 ("active", "pressed", "!disabled", "img_closepressed"),
                                 ("active", "!disabled", "img_closeactive"), border=8, sticky='e')
        except tk.TclError:
            pass

        style.layout("CloseableNotebook", [("CloseableNotebook.client", {"sticky": "nswe"})])

        style.layout("CloseableNotebook.Tab", [
            ("CloseableNotebook.tab", {
                "sticky": "nswe",
                "expand": 1,
                "children": [
                    ("CloseableNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CloseableNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CloseableNotebook.label", {"side": "left", "sticky": 'w'}),
                                    ("CloseableNotebook.close", {"side": "left", "sticky": 'e'}),
                                ]})
                        ]})
                ]})])


class DraggableNotebook(ttk.Notebook):
    """
    DraggableNotebook class.
    
    Allows the user to drag tabs around to reorder them. Subclass of the ttk::Notebook widget.
    
    Code partly translated from this Tcl/Tk snippet :
    https://wiki.tcl-lang.org/page/Drag+and+Drop+Notebook+Tabs
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._src_index = None
        self._toplevels = []
        self._children = []

        self.bind("<ButtonPress-1>", self._on_mouse_button_1_pressed)
        self.bind("<ButtonRelease-1>", self._on_mouse_button_1_released)
        self.bind("<B1-Motion>", self._on_mouse_button_1_motion)
        # self.bind("<<NotebookTabChanged>>", self._on_notebook_tab_changed)

    def _on_mouse_button_1_pressed(self, event=None):
        self._src_index = self.index(f'@{event.x},{event.y}')

    def _on_mouse_button_1_released(self, event=None):
        dst_index = None
        if isinstance(self._src_index, int):
            try:
                dst_index = self.index(f'@{event.x},{event.y}')
            except _tkinter.TclError:
                dst_index = None
            if isinstance(dst_index, int):
                tab = self.tabs()[self._src_index]
                self.insert(dst_index, tab)
    
    def _on_mouse_button_1_motion(self, event=None):
        # TODO: Pass down the event through the event queue to subwidgets
        # https://wiki.tcl-lang.org/page/Drag+and+Drop+Notebook+Tabs
        # https://wiki.tcl-lang.org/page/ttk::notebook
        # https://github.com/RedFantom/ttkwidgets/blob/master/ttkwidgets/table.py
        pass

    def _on_notebook_tab_changed(self, event=None):
        if self._mouse_button_1_pressed:
            self.insert(f"@{event.x},{event.y}", self.identify(*self._mouse_button_1_pressed))
    
    def _create_toplevel(self, child, tabkw):
        # TODO: Allow dragging the tabs to a new tkinter.Toplevel
        
        tl = tk.Toplevel(self)
        nb = DraggableNotebook(tl)
        child.master = nb
        nb.add(child, **tabkw)
        nb.pack()
        self._toplevels.append(tl)
    
    def add(self, child, **kw):
        rv = super().add(child, **kw)
        self._children.append(child)
        return rv
    
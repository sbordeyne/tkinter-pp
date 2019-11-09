import tkinter as tk
from . import utils


class Text(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        self.callbacks = kwargs.get("callbacks", [])
        del kwargs["callbacks"]
        tk.Canvas.__init__(self, *args, **kwargs)
        self.text_widget = None

    def attach(self, text_widget):
        self.text_widget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            for callback in self.callbacks:
                callback(i)
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.text_widget.index("%s+1line" % i)


class TextWithLineNumbers(tk.Frame):
    def __init__(self, master=None, line_numbers_callbacks=None, **text_kwargs):
        """
        Text widget with line numbers attached to it.
        :param master: Parent widget.
        :param line_numbers_callbacks: A list of callbacks that are triggered on every line number redraw.
                                       Redraws happen every time the widget is changed or configured.
                                       callbacks take an argument, which is the current line number being redrawn.
        :param text_kwargs: keyword arguments that are passed straight to the underlying tkinter.Text widget.
        """
        super().__init__(master)
        if line_numbers_callbacks is None:
            line_numbers_callbacks = []
        self.line_numbers_callbacks = line_numbers_callbacks
        self.text = Text(self, **text_kwargs)
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.text.yview)
        self.hsb = tk.Scrollbar(self, orient="horizontal",
                                command=self.text.xview)
        self.text.configure(yscrollcommand=lambda f, l: utils.auto_scroll(self.vsb, f, l),
                            xscrollcommand=lambda f, l: utils.auto_scroll(self.hsb, f, l),
                            wrap=tk.NONE,
                            undo=True)
        self.linenumbers = TextLineNumbers(self, width=30, callbacks=self.line_numbers_callbacks)
        self.linenumbers.attach(self.text)

        self.linenumbers.redraw()
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()

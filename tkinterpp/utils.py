def auto_scroll(sbar, first, last):
    """
    Hide and show scrollbar as needed.

    :param sbar: tk.Scrollbar to show/hide
    :param first: float representing the start point of the scrollbar
    :param last: float representing the end point of the scrollbar

    :returns: None, sets the scrollbar to the tuple (first, last) and shows/hides
    the scrollbar depending on whether it is necessary for it to show up or not.
    """
    first, last = float(first), float(last)
    if first <= 0 and last >= 1:
        sbar.grid_remove()
    else:
        sbar.grid()
    sbar.set(first, last)


def get_root_widget(widget):
    while widget.master is not None:
        widget = widget.master
    return widget

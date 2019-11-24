import textwrap
from tkinterpp.errors import I18NError


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


def i18n(text, dst_lang=None, wrapping=0):
    """
    Translates a text from a source lang to another.
    
    :param text: (required) source text to translate
    :param dst_lang: (default: None) dictionary mapping {src:dst} from source
                     lang to destination lang. Use tkinterpp.utils.get_i18n_dict to
                     load a matching dict from a file.
    :param wrapping: (default: 0) number of characters to wrap the resulting string at
                      using textwrap.wrap, long uninterrupted lines will still be wrapped at
                      the exact desired width. If wrapping <= 0, no wrapping will be applied.
    :return: translated text
    :raises: tkinterpp.errors.I18NError if dst_lang is not None or dict.
    """
    if dst_lang is None:
        return text if wrapping <= 0 else textwrap.wrap(text, wrapping)
    
    if isinstance(dst_lang, dict):
        dst_text = dst_lang.get(text, text)
        if wrapping > 0:
            dst_text = textwrap.wrap(dst_text, wrapping)
        return dst_text

    raise I18NError("dst_lang argument should be of type NoneType or dict")


def get_i18n_dict(file_path):
    """
    Gets a tkinterpp.utils.i18n compatible dictionary from a file.
    
    The file should be formatted as such :
    
    "Original language text" : "texte dans la langue originale"
    "Another string" : "Une autre chaîne de caractères"
    
    and so on.
    
    :param file_path: a path to the file to load
    :return: dict of <src>:<dst> pairs to use in i18n function.
    """
    rv = {}
    with open(file_path, "r") as f:
        for line in f:
            splits = line.split('"')
            key = splits[1]
            value = splits[-2]
            rv[key] = value
    return rv

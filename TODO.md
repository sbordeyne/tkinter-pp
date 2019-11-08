# IDEAS for tkinter widgets

## Generic

### TableView

A treeview dedicated to displaying tables. With sorting based on the headers

### FormFrame

A Frame dedicated to forms, with support for tk.Entry, ttk.Combobox, tk.Checkbutton, tk.Radiobutton

### NodeView

A Canvas-based widget to show a node graph, with events to bind to when a node is created, deleted, moved

### Calendar - DONE
```
A calendar, should return a datetime.datetime object.
TODO: Calendar should be a standalone widget, with a 7x5 grid
grid should be in order: Mon, Tue, Wed, Thu, Fri, Sat, Sun
option to set Sun as first day of the week ?
2 buttons, left/right to skip through the months like "< February >"
same for year
<   2019   >
< February >
M T W F S S
      1 2 3
4 5 6 7 8 9
Fire events on month/day/year changes
Entry widget that pops the calendar out?
ISO 8061 date format. No plebs here with their MM/DD/YYYY
```

## From tix

https://docs.python.org/3.7/library/tkinter.tix.html

### PopupMenu

A Menu that shows up on right click anywhere on the window.

### FileSelectBox

Change the current entry to be a combobox instead that remembers the last selected files

### DirList, DirTree

Should be compatible with pathlib.Path objects as well as str instances. Shows the directory in a Listbox or a Treeview depending.

## From pmw

http://pmw.sourceforge.net/doc/

# Generic TODO stuff

- [ ] Create samples for each widget
- [ ] Take screenshots of each widget
- [ ] Put screenshots in README.md
- [ ] Write documentation

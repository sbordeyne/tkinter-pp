# TODO: Calendar should be a standalone widget, with a 7x5 grid
# grid should be in order: Mon, Tue, Wed, Thu, Fri, Sat, Sun
# option to set Sun as first day of the week ?
# 2 buttons, left/right to skip through the months like "< February >"
# same for year
# <   2019   >
# < February >
# M T W F S S
#       1 2 3
# 4 5 6 7 8 9
# Fire events on month/day/year changes
# Entry widget that pops the calendar out?
# ISO 8061 date format. No plebs here with their MM/DD/YYYY

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import datetime
from calendar import monthrange
from .variables import DateVar
from .assets import arrow_left, arrow_left_mask, arrow_right, arrow_right_mask


class Calendar(tk.Frame):
    def __init__(self, master=None, current_date=None, variable=None):
        super().__init__(master)
        self.master = master
        self._current_date = current_date if current_date is not None else datetime.datetime.today()
        self.variable = variable if variable is not None else DateVar(self.current_date)

        self._year_var = tk.StringVar(value=str(self.current_date.year))
        self._month_var = tk.StringVar(value=self.current_date.strftime("%B"))
        self._day_vars = [tk.StringVar(value=" ") for _ in range(35)]
        self.setup_ui()
        self.update_calendar()

    def setup_ui(self):
        self.year_left_btn = tk.Button(self, text="◀", relief=tk.GROOVE,
                                       command=self.on_button_year_left)
        self.year_right_btn = tk.Button(self, text="▶", relief=tk.GROOVE,
                                        command=self.on_button_year_right)
        self.year_lbl = tk.Label(self, textvariable=self._year_var)

        self.month_left_btn = tk.Button(self, text="◀", relief=tk.GROOVE,
                                        command=self.on_button_month_left)
        self.month_right_btn = tk.Button(self, text="▶", relief=tk.GROOVE,
                                         command=self.on_button_month_right)
        self.month_lbl = tk.Label(self, textvariable=self._month_var)

        self.year_left_btn.grid(row=0, column=0)
        self.year_lbl.grid(row=0, column=2, columnspan=5)
        self.year_right_btn.grid(row=0, column=6)
        self.month_left_btn.grid(row=1, column=0)
        self.month_lbl.grid(row=1, column=2, columnspan=5)
        self.month_right_btn.grid(row=1, column=6)

        for i, day_name in enumerate(("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")):
            lbl = tk.Label(self, text=day_name)
            lbl.grid(row=2, column=i)

        self._day_buttons = [tk.Button(self, textvariable=var,
                                       command=lambda j=i:self._on_button_click(j),
                                       relief=tk.GROOVE, width=3, height=1,
                                       background="#EAEAEA")
                             for i, var in enumerate(self._day_vars)]
        for i, db in enumerate(self._day_buttons):
            db.bind('<FocusIn>', lambda evt, j=i: self._on_button_click(j))
            db.grid(row=i // 7 + 3, column=i % 7)

    def _on_button_click(self, iid):
        if not self._day_vars[iid].get().strip():
            return
        for btn in self._day_buttons:
            btn.config(background="#EAEAEA")
        self._day_buttons[iid].config(background="#0095FF")
        self.current_date = (None, None, int(self._day_vars[iid].get()))

    @property
    def current_date(self):
        return self._current_date

    @current_date.setter
    def current_date(self, value):
        year, month, day = value
        updater = {}
        if year is not None:
            updater["year"] = year
        if month is not None:
            updater["month"] = month
        if day is not None:
            updater["day"] = day

        self._current_date.replace(**updater)
        self.variable.set(self._current_date)

    def on_button_year_left(self):
        self.current_date = (self._current_date.year - 1, None, None)
        self.update_calendar()

    def on_button_year_right(self):
        self.current_date = (self._current_date.year + 1, None, None)
        self.update_calendar()

    def on_button_month_left(self):
        month = self.current_date.month - 1
        year = None
        if month == 0:
            month = 12
            year = self.current_date.year - 1
        self.current_date = (year, month, None)
        self.update_calendar()

    def on_button_month_right(self):
        month = self.current_date.month + 1
        year = None
        if month == 13:
            month = 1
            year = self.current_date.year + 1
        self.current_date = (year, month, None)
        self.update_calendar()

    def update_calendar(self):
        first_of_the_month_date = datetime.datetime.strptime(self.current_date.strftime("01 %m %Y"), "%d %m %Y")
        _first_of_the_month_weekday = first_of_the_month_date.weekday()
        _last_of_the_month_weekday = monthrange(self._current_date.year, self._current_date.month)[1] + \
            _first_of_the_month_weekday - 1

        for i in range(len(self._day_vars)):
            self._day_vars[i].set(" ")
            if _first_of_the_month_weekday <= i <= _last_of_the_month_weekday:
                self._day_vars[i].set(f"{i + 1 - _first_of_the_month_weekday}")
                self._day_buttons[i].config(textvariable=self._day_vars[i])
                if self._day_vars[i].get().strip():
                    self._day_buttons[i].config(state=tk.NORMAL)
                else:
                    self._day_buttons[i].config(state=tk.DISABLED)
        self._year_var.set(str(self.current_date.year))
        self._month_var.set(self.current_date.strftime("%B"))
        self.year_lbl.config(textvariable=self._year_var)
        self.month_lbl.config(textvariable=self._month_var)
        self._on_button_click(_first_of_the_month_weekday + self.current_date.day - 1)
        self.update()

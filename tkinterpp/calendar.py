try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import datetime
from calendar import monthrange
from .variables import DateVar


class Calendar(tk.Frame):
    def __init__(self, master=None, current_date=None, variable=None):
        super().__init__(master)
        self.master = master
        self.current_date = current_date if current_date is not None else datetime.datetime.today()
        self.variable = variable if variable is not None else DateVar(self.current_date)

        self._year_var = tk.StringVar(value=str(self.current_date.year))
        self._month_var = tk.StringVar(value=self.current_date.strftime("%B"))
        self._day_vars = [tk.StringVar(value=" ") for _ in range(42)]
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
        self.year_lbl.grid(row=0, column=2, columnspan=3)
        self.year_right_btn.grid(row=0, column=6)
        self.month_left_btn.grid(row=1, column=0)
        self.month_lbl.grid(row=1, column=2, columnspan=3)
        self.month_right_btn.grid(row=1, column=6)

        for i, day_name in enumerate(("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")):
            lbl = tk.Label(self, text=day_name)
            lbl.grid(row=2, column=i)

        self._day_buttons = [tk.Button(self, textvariable=var,
                                       command=lambda j=i:self.on_button_day(j),
                                       relief=tk.GROOVE, width=3, height=1,
                                       background="#EAEAEA")
                             for i, var in enumerate(self._day_vars)]
        for i, db in enumerate(self._day_buttons):
            db.bind('<FocusIn>', lambda evt, j=i: self.on_button_day(j))
            db.grid(row=i // 7 + 3, column=i % 7)

    def on_button_day(self, iid):
        if not self._day_vars[iid].get().strip():
            return
        for btn in self._day_buttons:
            btn.config(background="#EAEAEA")
        self._day_buttons[iid].config(background="#0095FF")
        self.set_current_date(None, None, int(self._day_vars[iid].get()))

    def set_current_date(self, year=None, month=None, day=None):
        updater = {}
        if year is not None:
            updater["year"] = year
        if month is not None:
            updater["month"] = month
        to_date_month_range = monthrange(updater.get("year", self.current_date.year),
                                         updater.get("month", self.current_date.month))
        if day is not None:
            updater["day"] = day
        elif self.current_date.day not in range(*to_date_month_range):
            updater["day"] = to_date_month_range[1]

        self.current_date = self.current_date.replace(**updater)
        self.variable.set(self.current_date)

    def on_button_year_left(self):
        self.set_current_date(self.current_date.year - 1, None, None)
        self.update_calendar()

    def on_button_year_right(self):
        self.set_current_date(self.current_date.year + 1, None, None)
        self.update_calendar()

    def on_button_month_left(self):
        month = self.current_date.month - 1
        year = None
        if month == 0:
            month = 12
            year = self.current_date.year - 1
        self.set_current_date(year, month, None)
        self.update_calendar()

    def on_button_month_right(self):
        month = self.current_date.month + 1
        year = None
        if month == 13:
            month = 1
            year = self.current_date.year + 1
        self.set_current_date(year, month, None)
        self.update_calendar()

    def update_calendar(self):
        first_of_the_month_date = datetime.datetime.strptime(self.current_date.strftime("01 %m %Y"), "%d %m %Y")
        _first_of_the_month_weekday = first_of_the_month_date.weekday()
        _last_of_the_month_weekday = monthrange(self.current_date.year, self.current_date.month)[1] + \
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
        self.on_button_day(_first_of_the_month_weekday + self.current_date.day - 1)
        self.update()

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

import tkinter as tk
import datetime
from .variables import DateVar
from .assets import arrow_left, arrow_left_mask, arrow_right, arrow_right_mask


class Calendar(tk.Frame):
    def __init__(self, master=None, current_date=None, variable=None):
        super().__init__(master)
        self.master = master
        self.current_date = current_date if current_date is not None else datetime.datetime.today()
        self.variable = variable if variable is not None else DateVar(self.current_date)

        self._year_var = tk.StringVar(value=str(self.current_date.year))
        self._month_var = tk.StringVar(value=self.current_date.strftime("%B"))
        first_of_the_month_date = datetime.datetime.strptime(self.current_date.strftime("01 %m %Y"), "%d %m %Y")
        self._first_of_the_month_weekday = first_of_the_month_date.weekday()
        self._day_vars = [tk.StringVar(value=" ") for _ in range(35)]

    def setup_ui(self):
        self._day_buttons = [tk.Button(self, textvariable=var,
                                       command=lambda : self._on_button_click(i))
                             for i, var in enumerate(self._day_vars)]

    def _on_button_click(self, iid):
        pass

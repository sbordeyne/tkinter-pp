import datetime
from copy import copy


class DateVar:
    def __init__(self, date=None):
        self.date = self._parse_date(date)
        self.traces = {"read": [],
                       "write": [],
                       "unset": []}

    @staticmethod
    def _parse_date(date=None):
        return date if date is not None else datetime.datetime.today()

    def get(self):
        for _, cb in self.traces["read"]:
            cb()
        return self.date

    def set(self, date=None):
        for _, cb in self.traces["write"]:
            cb()
        self.date = self._parse_date(date)

    def trace_add(self, mode, callback):
        """
        Define a trace callback for the variable.

        Mode is one of "read", "write", "unset", or a list or tuple of
        such strings.
        Callback must be a function which is called when the variable is
        read, written or unset.

        Return the name of the callback.
        """
        if isinstance(mode, str):
            mode = [mode]
        for m in mode:
            self.traces[m].append((callback.__name__, callback))
        return callback.__name__

    def trace_remove(self, mode, cbname):
        """
        Delete the trace callback for a variable.

        Mode is one of "read", "write", "unset" or a list or tuple of
        such strings.  Must be same as were specified in trace_add().
        cbname is the name of the callback returned from trace_add().
        """
        if isinstance(mode, str):
            mode = [mode]

        for m in mode:
            indices = [i for i, cb in enumerate(self.traces[m]) if cb[0] == cbname]
            for nb, i in enumerate(indices):
                self.traces[m].pop(i - nb)

    def trace_info(self):
        """
        Return all trace callback information.
        """
        return copy(self.traces)

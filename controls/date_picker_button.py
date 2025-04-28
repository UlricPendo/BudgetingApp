from flet import ElevatedButton, DatePicker, ControlEvent
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class DatePickerButton(ElevatedButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.date_picker = DatePicker(
            first_date=date.today() - relativedelta(years=1),
            last_date=date.today() + relativedelta(years=1),
            # on_change=handle_change,
            # on_dismiss=handle_dismissal,
        )

        self.on_click = self.open_date_picker

    def open_date_picker(self, event: ControlEvent) -> None:
        self.page.open(self.date_picker)
        self.page.update()


"""
on dismiss save to txt
date + income added
draw date to screen
same income 2 diff dates, update one

5 tues, 5 wed reality
wrote in correct both tues
"""


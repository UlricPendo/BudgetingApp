from flet import (
    ElevatedButton,
    Column,
)


class startDate(Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.dateselect = ElevatedButton("Pick Date")

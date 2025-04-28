from flet import (
    DatePicker,
    ElevatedButton,
    Column,
    Row,
    Text,
    MainAxisAlignment,
    Icon,
    Page,
    DatePickerEntryMode,
    DatePickerEntryModeChangeEvent,
    DatePickerTheme,
    DatePickerMode,
)
import datetime


class startDate(Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.dateselect = ElevatedButton("Pick Date")

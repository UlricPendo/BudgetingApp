from flet import View, Row
from controls.income_input import IncomeInput
from controls.date_picker_button import DatePickerButton


class BudgetPage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(route="/Budget", *args, **kwargs)

        self.controls = [
            DatePickerButton(text="Select Start Date"),
            Row(controls=[IncomeInput(), IncomeInput()]),
        ]

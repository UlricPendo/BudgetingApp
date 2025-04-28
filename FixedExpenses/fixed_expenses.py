from flet import (
    Column,
    TextField,
    ElevatedButton,
    Row,
    Text,
    MainAxisAlignment,
    NumbersOnlyInputFilter,
    InputFilter,
)
from IncomeInput.Income_Btn_Input import AddIncome


class fExpensesInput(Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.width = 300
        self.expense_input = TextField(
            label="Enter in Fixed Expenses(Numbers only)",
            width=300,
            # keyboard_type="number", # for mobile keyboard display
            input_filter=NumbersOnlyInputFilter(),
        )
        self.Expense_row = Row(alignment=MainAxisAlignment.START)
        self.Expense_stored = Text("Expense Added:")
        self.Expense_column = Column()
        self.total_Expense = Text("Total Expenses:")

        self.controls = [
            self.expense_input,
            Row(
                controls=[
                    AddIncome("Add Expense"),
                ],
                alignment=MainAxisAlignment.START,
            ),
            self.Expense_stored,
            self.Expense_row,
            self.total_Expense,
        ]

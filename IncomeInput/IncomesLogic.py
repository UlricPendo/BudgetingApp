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

# attempted to seperate everything into its own files to keep it more orginized but i am struggling.


class incomeStorage(Column):
    def __init__(self, e):
        super().__init__()
        self.expand = True

    def add_income(self, e):
        if self.income_input.value:
            self.incomes.append(float(self.income_input.value))
            new_income = Text(self.income_input.value)
            # Add the new Text component to the Column
            self.income_column.controls.append(new_income)
            self.total_income.value = f"Total Income: ${sum(self.incomes):.2f}"
            self.income_input.value = ""
            self.update()

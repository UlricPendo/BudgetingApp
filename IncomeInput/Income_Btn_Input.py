from flet import ElevatedButton, ControlEvent, Text


class AddIncome(ElevatedButton):
    def __init__(self, float):
        super().__init__(float)
        self.expand = True
        self.on_click = self.clicked

    # def clicked(self, event: ControlEvent) -> None:
    #     income = self.page.controls[0]
    #     income.income_added += income.income_input
    #     income.income_row = [Text(value=income.income_added)]
    #     self.page.update()
    def clicked(self, event: ControlEvent) -> None:
        try:
            value = float(self.income_input.value)
            self.incomes.append(value)
            new_income = Text(f"Income: ${self.income_input.value}")
            self.income_column.controls.append(new_income)
            self.total_income.value = f"Total Income: ${sum(self.incomes):.2f}"
            self.income_input.value = ""
            self.income_input.error_text = None
        except ValueError:
            self.income_input.error_text = "Please enter a valid number!"
        self.page.update()


# class RemoveIncome(ElevatedButton):
#     def __init__(self, text):
#         super().__init__(text)
#         self.expand = True
#         self.on_click = self.clicked

#     def clicked(self, event: ControlEvent) -> None:
#         addIn = self.page.controls[0]
#         addIn.expression += str(self.text)
#         addIn.expressoin_row.controls = [Text(value=addIn.expression)]
#         self.page.update()

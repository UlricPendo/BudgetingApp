from flet import (
    Column,
    TextField,
    ElevatedButton,
    Row,
    Text,
    MainAxisAlignment,
    NumbersOnlyInputFilter,
    Container,
    Colors,
    TextStyle,
    FontWeight,
    ResponsiveRow,
    TextOnlyInputFilter,
    OnFocusEvent,
)


class IncomeInput(Column):
    def __init__(self):
        super().__init__()
        self.expand = True

        # self.width = 300
        self.income_row = Row(alignment=MainAxisAlignment.START)
        addincome = self.add_income_btn = ElevatedButton(
            "Add Income", on_click=self.add_income
        )
        removeincome = self.remove_income_btn = ElevatedButton(
            "Remove Income", on_click=self.remove_income
        )
        tfbgC = Colors.GREY_300

        incomeTypeinput = self.incomeTypeinput = TextField(
            label="Description",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            bgcolor="white",
            focused_bgcolor=tfbgC,
            hint_text="eg, Salary, Freelance",
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
            input_filter=TextOnlyInputFilter(),
        )
        incomeAmountinput = self.income_input = TextField(
            label="Amount($)",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            hint_text="0.00",
            bgcolor="white",
            focused_bgcolor=tfbgC,
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
            input_filter=NumbersOnlyInputFilter(),
        )
        incomeDateinput = self.incomeDateinput = TextField(
            label="Date",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            hint_text="DD/MM/YY",
            bgcolor="white",
            focused_bgcolor=tfbgC,
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
        )
        ilabel = self.incomeLabel = Text(
            "Income", color="black", size=30, weight=FontWeight.BOLD
        )
        isubheader = self.subheader = Text("Manage your Income sources", color="black")
        addedIncome = self.income_column = Column()
        tincome = self.total_income = Text(
            "Total Income: $0.00", color="black", weight=FontWeight.W_600
        )

        inputs = self.inputs = ResponsiveRow(
            [incomeTypeinput, incomeAmountinput, incomeDateinput],
            run_spacing={"xs": 10},
        )

        self.IncomeContainer = Container(
            bgcolor="white",
            expand=True,
            border_radius=15,
            padding=10,
            margin=10,
            # content=Text("Income Input"),
            content=Column(
                expand=True,
                controls=[
                    ilabel,
                    isubheader,
                    inputs,
                    Row(controls=[addincome, removeincome]),
                    Text("Income Added:", color="black", weight="bold"),
                    addedIncome,
                    tincome,
                ],
            ),
        )

        # draws onto screen
        self.controls = [
            self.IncomeContainer,
        ]
        # array to store entered incomes.
        self.incomes = []

    # chatgpt helped with this
    def add_income(self, e):
        # not sure what try is
        try:
            # gives the variable value the properties of a float, and passes the income_input value to it
            value = float(self.income_input.value)
            # passes value into incomes array
            self.incomes.append(value)
            # passes the value into a text to be displayed
            new_income = Text(
                f"{self.incomeTypeinput.value} | ${self.income_input.value} | {self.incomeDateinput.value} ",
                color="black",
            )
            # creates a new column with the properties of new_income
            self.income_column.controls.append(new_income)
            # adds the values inside the incomes array, and passes to total_income to be displayed
            self.total_income.value = f"Total Income: ${sum(self.incomes):.2f}"
            # removes the text inside of the textfield to be blank
            self.income_input.value = ""
            self.incomeDateinput.value = ""
            self.incomeTypeinput.value = ""
            self.income_input.error_text = None  # Clear error if successful
        except ValueError:
            # error handling, if no value is entered or if they try to enter something weird that isnt handled by the input filter
            self.income_input.error_text = "Please enter a valid number!"

        self.update()

    # chatgpt helped with this
    def remove_income(self, e):
        # checks if there is something in incomes[], if there is do self.incomes.pop()<- not sure what pop() does. assuming it removes last thing in the array
        if self.incomes:
            self.incomes.pop()  # Remove the last added income
            # after removing from the last inputed thing in array, checks if there has been a new column added? and removes it im assuming
            if self.income_column.controls:
                self.income_column.controls.pop()  # Remove the last displayed Text
            # this is re-adding everything thats stored in incomes
            total = sum(self.incomes)
            # passing the value of total to total_income to be desplayed
            self.total_income.value = f"Total Income: ${total:.2f}"
        else:
            # error handling, if they try to remove income with no income added.
            self.income_input.error_text = "No income to remove!"
        self.update()

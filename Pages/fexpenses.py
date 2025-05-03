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


class fExpenseInput(Column):
    def __init__(self):
        super().__init__()
        self.expand = True

        # self.width = 300
        self.fExpense_row = Row(alignment=MainAxisAlignment.START)
        addfExpense = self.add_fExpense_btn = ElevatedButton(
            "Add Fixed Expense", on_click=self.add_fExpense
        )
        removefExpense = self.remove_fExpense_btn = ElevatedButton(
            "Remove Fixed Expense", on_click=self.remove_fExpense
        )
        tfbgC = Colors.GREY_300

        fExpenseTypeinput = self.fExpenseTypeinput = TextField(
            label="Description",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            bgcolor="white",
            focused_bgcolor=tfbgC,
            hint_text="eg, Rent, Phone bill",
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
            input_filter=TextOnlyInputFilter(),
        )
        fExpenseAmountinput = self.fExpense_input = TextField(
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
        fExpenseDateinput = self.fExpenseDateinput = TextField(
            label="Date",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            hint_text="DD/MM/YY",
            bgcolor="white",
            focused_bgcolor=tfbgC,
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
        )
        ilabel = self.fExpenseLabel = Text(
            "Fixed Expense", color="black", size=30, weight=FontWeight.BOLD
        )
        isubheader = self.subheader = Text(
            "Manage your Fixed Expense sources", color="black"
        )
        addedfExpense = self.fExpense_column = Column()
        tfExpense = self.total_fExpense = Text(
            "Total Fixed Expense: $0.00", color="black", weight=FontWeight.W_600
        )

        inputs = self.inputs = ResponsiveRow(
            [fExpenseTypeinput, fExpenseAmountinput, fExpenseDateinput],
            run_spacing={"xs": 10},
        )

        self.fExpenseContainer = Container(
            bgcolor="white",
            expand=True,
            border_radius=15,
            padding=10,
            margin=10,
            # content=Text("fExpense Input"),
            content=Column(
                expand=True,
                controls=[
                    ilabel,
                    isubheader,
                    inputs,
                    Row(controls=[addfExpense, removefExpense]),
                    Text("Fixed Expense Added:", color="black", weight="bold"),
                    addedfExpense,
                    tfExpense,
                ],
            ),
        )

        # draws onto screen
        self.controls = [
            self.fExpenseContainer,
        ]
        # array to store entered fExpenses.
        self.fExpenses = []

    # chatgpt helped with this
    def add_fExpense(self, e):
        # not sure what try is
        try:
            # gives the variable value the properties of a float, and passes the fExpense_input value to it
            value = float(self.fExpense_input.value)
            # passes value into fExpenses array
            self.fExpenses.append(value)
            # passes the value into a text to be displayed
            new_fExpense = Text(
                f"{self.fExpenseTypeinput.value} | ${self.fExpense_input.value} | {self.fExpenseDateinput.value} ",
                color="black",
            )
            # creates a new column with the properties of new_fExpense
            self.fExpense_column.controls.append(new_fExpense)
            # adds the values inside the fExpenses array, and passes to total_fExpense to be displayed
            self.total_fExpense.value = (
                f"Total Fixed Expense: ${sum(self.fExpenses):.2f}"
            )
            # removes the text inside of the textfield to be blank
            self.fExpense_input.value = ""
            self.fExpenseDateinput.value = ""
            self.fExpenseTypeinput.value = ""
            self.fExpense_input.error_text = None  # Clear error if successful
        except ValueError:
            # error handling, if no value is entered or if they try to enter something weird that isnt handled by the input filter
            self.fExpense_input.error_text = "Please enter a valid number!"

        self.update()

    # chatgpt helped with this
    def remove_fExpense(self, e):
        # checks if there is something in fExpenses[], if there is do self.fExpenses.pop()<- not sure what pop() does. assuming it removes last thing in the array
        if self.fExpenses:
            self.fExpenses.pop()  # Remove the last added fExpense
            # after removing from the last inputed thing in array, checks if there has been a new column added? and removes it im assuming
            if self.fExpense_column.controls:
                self.fExpense_column.controls.pop()  # Remove the last displayed Text
            # this is re-adding everything thats stored in fExpenses
            total = sum(self.fExpenses)
            # passing the value of total to total_fExpense to be desplayed
            self.total_fExpense.value = f"Total Fixed Expense: ${total:.2f}"
        else:
            # error handling, if they try to remove fExpense with no fExpense added.
            self.fExpense_input.error_text = "No Fixed Expense to remove!"
        self.update()

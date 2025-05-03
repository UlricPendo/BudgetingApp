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


class vExpenseInput(Column):
    def __init__(self):
        super().__init__()
        self.expand = True

        # self.width = 300
        self.vExpense_row = Row(alignment=MainAxisAlignment.START)
        addvExpense = self.add_vExpense_btn = ElevatedButton(
            "Add Variable Expense", on_click=self.add_vExpense
        )
        removevExpense = self.remove_vExpense_btn = ElevatedButton(
            "Remove Variable Expense", on_click=self.remove_vExpense
        )
        tfbgC = Colors.GREY_300

        vExpenseTypeinput = self.vExpenseTypeinput = TextField(
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
        vExpenseAmountinput = self.vExpense_input = TextField(
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
        vExpenseDateinput = self.vExpenseDateinput = TextField(
            label="Date",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            hint_text="DD/MM/YY",
            bgcolor="white",
            focused_bgcolor=tfbgC,
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
        )
        ilabel = self.vExpenseLabel = Text(
            "Variable Expense", color="black", size=30, weight=FontWeight.BOLD
        )
        isubheader = self.subheader = Text(
            "Manage your Variable Expense sources", color="black"
        )
        addedvExpense = self.vExpense_column = Column()
        tvExpense = self.total_vExpense = Text(
            "Total Variable Expense: $0.00", color="black", weight=FontWeight.W_600
        )

        inputs = self.inputs = ResponsiveRow(
            [vExpenseTypeinput, vExpenseAmountinput, vExpenseDateinput],
            run_spacing={"xs": 10},
        )

        self.vExpenseContainer = Container(
            bgcolor="white",
            expand=True,
            border_radius=15,
            padding=10,
            margin=10,
            # content=Text("vExpense Input"),
            content=Column(
                expand=True,
                controls=[
                    ilabel,
                    isubheader,
                    inputs,
                    Row(controls=[addvExpense, removevExpense]),
                    Text("Variable Expense Added:", color="black", weight="bold"),
                    addedvExpense,
                    tvExpense,
                ],
            ),
        )

        # draws onto screen
        self.controls = [
            self.vExpenseContainer,
        ]
        # array to store entered vExpenses.
        self.vExpenses = []

    # chatgpt helped with this
    def add_vExpense(self, e):
        # not sure what try is
        try:
            # gives the variable value the properties of a float, and passes the vExpense_input value to it
            value = float(self.vExpense_input.value)
            # passes value into vExpenses array
            self.vExpenses.append(value)
            # passes the value into a text to be displayed
            new_vExpense = Text(
                f"{self.vExpenseTypeinput.value} | ${self.vExpense_input.value} | {self.vExpenseDateinput.value} ",
                color="black",
            )
            # creates a new column with the properties of new_vExpense
            self.vExpense_column.controls.append(new_vExpense)
            # adds the values inside the vExpenses array, and passes to total_vExpense to be displayed
            self.total_vExpense.value = (
                f"Total Variable Expense: ${sum(self.vExpenses):.2f}"
            )
            # removes the text inside of the textfield to be blank
            self.vExpense_input.value = ""
            self.vExpenseDateinput.value = ""
            self.vExpenseTypeinput.value = ""
            self.vExpense_input.error_text = None  # Clear error if successful
        except ValueError:
            # error handling, if no value is entered or if they try to enter something weird that isnt handled by the input filter
            self.vExpense_input.error_text = "Please enter a valid number!"

        self.update()

    # chatgpt helped with this
    def remove_vExpense(self, e):
        # checks if there is something in vExpenses[], if there is do self.vExpenses.pop()<- not sure what pop() does. assuming it removes last thing in the array
        if self.vExpenses:
            self.vExpenses.pop()  # Remove the last added vExpense
            # after removing from the last inputed thing in array, checks if there has been a new column added? and removes it im assuming
            if self.vExpense_column.controls:
                self.vExpense_column.controls.pop()  # Remove the last displayed Text
            # this is re-adding everything thats stored in vExpenses
            total = sum(self.vExpenses)
            # passing the value of total to total_vExpense to be desplayed
            self.total_vExpense.value = f"Total Variable Expense: ${total:.2f}"
        else:
            # error handling, if they try to remove vExpense with no vExpense added.
            self.vExpense_input.error_text = "No Variable Expense to remove!"
        self.update()

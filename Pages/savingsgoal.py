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


class SavingsGoalInput(Column):
    def __init__(self):
        super().__init__()
        self.expand = True

        # self.width = 300
        self.SavingsGoal_row = Row(alignment=MainAxisAlignment.START)
        addSavingsGoal = self.add_SavingsGoal_btn = ElevatedButton(
            "Add Savings Goal", on_click=self.add_SavingsGoal
        )
        removeSavingsGoal = self.remove_SavingsGoal_btn = ElevatedButton(
            "Remove Savings Goal", on_click=self.remove_SavingsGoal
        )
        tfbgC = Colors.GREY_300

        SavingsGoalTypeinput = self.SavingsGoalTypeinput = TextField(
            label="Description",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            bgcolor="white",
            focused_bgcolor=tfbgC,
            hint_text="eg, Flight, Game",
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
            input_filter=TextOnlyInputFilter(),
        )
        SavingsGoalAmountinput = self.SavingsGoal_input = TextField(
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
        SavingsGoalDateinput = self.SavingsGoalDateinput = TextField(
            label="Target Date(Optional)",
            label_style=TextStyle(color="black", weight="bold"),
            text_style=TextStyle(color="black"),
            hint_text="DD/MM/YY",
            bgcolor="white",
            focused_bgcolor=tfbgC,
            col={"xs": 12, "md": 4},
            # keyboard_type="number", # for mobile keyboard display
        )
        ilabel = self.SavingsGoalLabel = Text(
            "Savings Goal", color="black", size=30, weight=FontWeight.BOLD
        )
        isubheader = self.subheader = Text(
            "Manage your Savings Goal sources", color="black"
        )
        addedSavingsGoal = self.SavingsGoal_column = Column()
        tSavingsGoal = self.total_SavingsGoal = Text(
            "Total Savings Goal: $0.00", color="black", weight=FontWeight.W_600
        )

        inputs = self.inputs = ResponsiveRow(
            [SavingsGoalTypeinput, SavingsGoalAmountinput, SavingsGoalDateinput],
            run_spacing={"xs": 10},
        )

        self.SavingsGoalContainer = Container(
            bgcolor="white",
            expand=True,
            border_radius=15,
            padding=10,
            margin=10,
            # content=Text("SavingsGoal Input"),
            content=Column(
                expand=True,
                controls=[
                    ilabel,
                    isubheader,
                    inputs,
                    Row(controls=[addSavingsGoal, removeSavingsGoal]),
                    Text("Savings Goal Added:", color="black", weight="bold"),
                    addedSavingsGoal,
                    tSavingsGoal,
                ],
            ),
        )

        # draws onto screen
        self.controls = [
            self.SavingsGoalContainer,
        ]
        # array to store entered SavingsGoals.
        self.SavingsGoals = []

    # chatgpt helped with this
    def add_SavingsGoal(self, e):
        # not sure what try is
        try:
            # gives the variable value the properties of a float, and passes the SavingsGoal_input value to it
            value = float(self.SavingsGoal_input.value)
            # passes value into SavingsGoals array
            self.SavingsGoals.append(value)
            # passes the value into a text to be displayed
            new_SavingsGoal = Text(
                f"{self.SavingsGoalTypeinput.value} | ${self.SavingsGoal_input.value} | {self.SavingsGoalDateinput.value} ",
                color="black",
            )
            # creates a new column with the properties of new_SavingsGoal
            self.SavingsGoal_column.controls.append(new_SavingsGoal)
            # adds the values inside the SavingsGoals array, and passes to total_SavingsGoal to be displayed
            self.total_SavingsGoal.value = (
                f"Total Savings Goal: ${sum(self.SavingsGoals):.2f}"
            )
            # removes the text inside of the textfield to be blank
            self.SavingsGoal_input.value = ""
            self.SavingsGoalDateinput.value = ""
            self.SavingsGoalTypeinput.value = ""
            self.SavingsGoal_input.error_text = None  # Clear error if successful
        except ValueError:
            # error handling, if no value is entered or if they try to enter something weird that isnt handled by the input filter
            self.SavingsGoal_input.error_text = "Please enter a valid number!"

        self.update()

    # chatgpt helped with this
    def remove_SavingsGoal(self, e):
        # checks if there is something in SavingsGoals[], if there is do self.SavingsGoals.pop()<- not sure what pop() does. assuming it removes last thing in the array
        if self.SavingsGoals:
            self.SavingsGoals.pop()  # Remove the last added SavingsGoal
            # after removing from the last inputed thing in array, checks if there has been a new column added? and removes it im assuming
            if self.SavingsGoal_column.controls:
                self.SavingsGoal_column.controls.pop()  # Remove the last displayed Text
            # this is re-adding everything thats stored in SavingsGoals
            total = sum(self.SavingsGoals)
            # passing the value of total to total_SavingsGoal to be desplayed
            self.total_SavingsGoal.value = f"Total Savings Goal: ${total:.2f}"
        else:
            # error handling, if they try to remove SavingsGoal with no SavingsGoal added.
            self.SavingsGoal_input.error_text = "No Savings Goal to remove!"
        self.update()

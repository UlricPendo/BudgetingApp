from flet import (
    Text,
    Colors,
    Container,
    CupertinoSlidingSegmentedButton,
    padding,
    Column,
    SnackBar,
    Row,
)
from Pages.income import IncomeInput
from Pages.fexpenses import fExpenseInput
from Pages.vexpenses import vExpenseInput
from Pages.emergfun import EmergancyFund
from Pages.savingsgoal import SavingsGoalInput
from Pages.trends import Budgettrends


class PageSwitch(Column):
    def __init__(self):
        super().__init__()
        self.expand = True

        self.pages = [
            IncomeInput(),
            fExpenseInput(),
            vExpenseInput(),
            EmergancyFund(),
            SavingsGoalInput(),
            Budgettrends(),
        ]

        self.page_selected = Container(content=self.pages[0], expand=True)

        def page_change(event):
            selected_index = event.control.selected_index
            self.page_selected.content = self.pages[selected_index]
            self.page_selected.update()

        Pageselect = self.Page_selector = CupertinoSlidingSegmentedButton(
            expand=True,
            selected_index=0,
            thumb_color=Colors.BLACK,
            on_change=page_change,
            controls=[
                Text("Income"),
                Text("Fixed Expenses"),
                Text("Variable Expenses"),
                Text("Emergancy Fund"),
                Text("Savings Goal(s)"),
                Text("Budget Trends"),
            ],
        )

        self.page_container = Container(
            expand=True,
            content=Column(
                expand=True,
                controls=[
                    Row(controls=[Pageselect]),
                    Row(controls=[self.page_selected]),
                ],
            ),
        )

        self.controls = [self.page_container]

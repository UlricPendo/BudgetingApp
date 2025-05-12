from flet import (
    Container,
    Text,
    DatePicker,
    ElevatedButton,
    Page,
    app,
    Icons,
    NavigationBar,
    NavigationBarDestination,
    ControlEvent,
    RouteChangeEvent,
    Row,
)

from Pages.summary import BudgetSummary
from Pages.income import IncomeInput
from Pages.fexpenses import fExpenseInput
from Pages.vexpenses import vExpenseInput
from Pages.emergfun import EmergancyFund
from Pages.savingsgoal import SavingsGoalInput
from Pages.trends import Budgettrends
from Pages.savings import SavingsSummary
from PageSwitcher.pageswitcher import PageSwitch


def main(page: Page):
    page.title = "Budget Tracker"
    page.vertical_alignment = "start"
    page.padding = 20
    page.bgcolor = "white"
    page.add(
        Row(controls=[BudgetSummary(), SavingsSummary()]), Row(controls=[PageSwitch()])
    )


app(target=main)

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

# ROUTES = ["/Income", "/fExpense", "/vExpense", "/EmergFund", "/SavingsGoal", "/Trends"]


# def handle_route_change(event: RouteChangeEvent) -> None:
#     event.page.controls.clear()
#     if event.route == "/Income":
#         event.page.add(
#             Row(
#                 controls=[BudgetSummary(), SavingsSummary()],
#             ),
#             Row(controls=[PageSwitch()]),
#             Row(controls=[IncomeInput()]),
#         )
#     elif event.route == "/fExpense":
#         event.page.add(
#             Row(
#                 controls=[BudgetSummary(), SavingsSummary()],
#             ),
#             Row(controls=[fExpenseInput()]),
#         )
#     elif event.route == "/vExpense":
#         event.page.add(
#             Row(
#                 controls=[BudgetSummary(), SavingsSummary()],
#             ),
#             Row(controls=[vExpenseInput()]),
#         )
#     elif event.route == "/EmergFund":
#         event.page.add(
#             Row(
#                 controls=[BudgetSummary(), SavingsSummary()],
#             ),
#             Row(controls=[EmergancyFund()]),
#         )
#     elif event.route == "/SavingsGoal":
#         event.page.add(
#             Row(
#                 controls=[BudgetSummary(), SavingsSummary()],
#             ),
#             Row(controls=[SavingsGoalInput()]),
#         )
#     else:
#         event.page.add(
#             Row(
#                 controls=[BudgetSummary(), SavingsSummary()],
#             ),
#             Row(controls=[Budgettrends()]),
#         )


# def change_route(event: ControlEvent) -> None:
#     event.page.go(ROUTES[event.control.selected_index])


def main(page: Page):
    page.title = "Budget Tracker"
    page.vertical_alignment = "start"
    page.padding = 20

    page.add(
        Row(controls=[BudgetSummary(), SavingsSummary()]), Row(controls=[PageSwitch()])
    )
    # page.on_route_change = handle_route_change
    # page.navigation_bar = NavigationBar(
    #     destinations=[
    #         NavigationBarDestination(icon=Icons.MONEY, label="Income"),
    #         NavigationBarDestination(icon=Icons.CREDIT_CARD, label="Fixed Expense"),
    #         NavigationBarDestination(
    #             icon=Icons.CREDIT_CARD_OFF_ROUNDED, label="Variable Expense"
    #         ),
    #         NavigationBarDestination(icon=Icons.WB_TWIGHLIGHT, label="Emergancy Fund"),
    #         NavigationBarDestination(icon=Icons.SAVINGS, label="Savings Goal"),
    #         NavigationBarDestination(icon=Icons.TRENDING_UP, label="Budget Trends"),
    #     ],
    # on_change=change_route,

    # page.go(route="/Income")


app(target=main)

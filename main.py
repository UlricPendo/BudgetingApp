from flet import (
    Page,
    app,
    Row,
    NavigationBar,
    NavigationBarDestination,
    Icons,
    RouteChangeEvent,
    ControlEvent,
    Text,
)

# Import only needed classes and functions
from IncomeInput.Incomeinput import IncomeInput
from FixedExpenses.fixed_expenses import fExpensesInput


ROUTES = ["/Budget", "/Graphs", "/History"]


def handle_route_change(event: RouteChangeEvent) -> None:
    event.page.controls.clear()
    if event.route == "/Budget":
        event.page.add(
            Row(
                controls=[IncomeInput(), fExpensesInput()],
            )
        )
    elif event.route == "/Graphs":
        event.page.add(Text("Graphs"))
    else:
        event.page.add(Text("History"))


def change_route(event: ControlEvent) -> None:
    event.page.go(ROUTES[event.control.selected_index])


def main(page: Page):
    page.title = "Budget Tracker"
    page.vertical_alignment = "start"
    page.padding = 20
    page.on_route_change = handle_route_change
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationBarDestination(icon=Icons.BOOK, label="Budget"),
            NavigationBarDestination(icon=Icons.AUTO_GRAPH, label="Graphs"),
            NavigationBarDestination(icon=Icons.HISTORY, label="History"),
        ],
        on_change=change_route,
    )

    page.go(route="/Budget")


app(target=main)

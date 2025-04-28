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
from Pages.income import IncomeInput


ROUTES = ["/Income", "/Fixed Expenses", "/Trends"]


def handle_route_change(event: RouteChangeEvent) -> None:
    event.page.controls.clear()
    if event.route == "/Income":
        event.page.add(
            Row(
                controls=[IncomeInput()],
            )
        )
    elif event.route == "/Fixed Expenses":
        event.page.add(Text("Fixed Expenses"))
    else:
        event.page.add(Text("Trends"))


def change_route(event: ControlEvent) -> None:
    event.page.go(ROUTES[event.control.selected_index])


def main(page: Page):
    page.title = "Income Tracker"
    page.vertical_alignment = "start"
    page.padding = 20
    page.on_route_change = handle_route_change
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationBarDestination(icon=Icons.BOOK, label="Income"),
            NavigationBarDestination(icon=Icons.AUTO_GRAPH, label="Fixed Expenses"),
            NavigationBarDestination(icon=Icons.HISTORY, label="Trends"),
        ],
        on_change=change_route,
    )

    page.go(route="/Income")


app(target=main)

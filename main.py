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
    View,
    Theme,
    PageTransitionTheme,
    PageTransitionsTheme,
)


from pages.budget import BudgetPage


ROUTES = ["/Budget", "/Graphs", "/History"]


def handle_route_change(event: RouteChangeEvent) -> None:
    event.page.views.pop()
    if event.route == "/Budget":
        event.page.views.append(BudgetPage(navigation_bar=event.page.navigation_bar))
    elif event.route == "/Graphs":
        event.page.views.append(
            View(controls=[Text("Graphs")], navigation_bar=event.page.navigation_bar)
        )
    else:
        event.page.views.append(
            View(controls=[Text("History")], navigation_bar=event.page.navigation_bar)
        )

    event.page.update()


def change_route(event: ControlEvent) -> None:
    event.page.go(ROUTES[event.control.selected_index])


def main(page: Page):
    page.title = "Budget Tracker"
    page.vertical_alignment = "start"
    page.padding = 20
    page.theme = Theme(
        page_transitions=PageTransitionsTheme(windows=PageTransitionTheme.NONE)
    )
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

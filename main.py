from flet import (
    Page,
    app,
    Row,
    MainAxisAlignment,
    Container,
    Text,
    alignment,
    NavigationBar,
    NavigationBarDestination,
    Icons,
)

# Import only needed classes and functions
from IncomeInput.Incomeinput import IncomeInput
from DatePicker.startdate import startDate
from FixedExpenses.fixed_expenses import fExpensesInput


def main(page: Page):
    page.title = "Budget Tracker"
    page.vertical_alignment = "start"
    page.padding = 20
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationBarDestination(icon=Icons.BOOK, label="Budget"),
            NavigationBarDestination(icon=Icons.AUTO_GRAPH, label="Graphs"),
            NavigationBarDestination(icon=Icons.HISTORY, label="History"),
        ]
    )
    # Call components to main
    income_section = IncomeInput()
    fExpenses = fExpensesInput()
    # Add all sections to the page
    page.add(
        Row(
            controls=[
                # Container(
                #     content=Text("Test"),
                #     padding=10,
                #     margin=10,
                #     bgcolor="white",
                #     alignment=alignment.center,
                #     # content=income_section,
                #     width=300,
                #     height=600,
                #     border_radius=10,
                # ),
                income_section,
                fExpenses,
            ],
        )
    )


app(target=main)

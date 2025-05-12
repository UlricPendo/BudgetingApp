from flet import (
    Container,
    Text,
    Colors,
    Column,
    FontWeight,
    Divider,
    Row,
    MainAxisAlignment,
    alignment,
    TextAlign,
    CrossAxisAlignment,
)


class BudgetSummary(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = "white"
        self.height = 300
        self.border_radius = 15
        self.padding = 20
        self.margin = 5
        self.total_income = Text(
            "$0",
            color="green",
            weight=FontWeight.BOLD,
            text_align=TextAlign.RIGHT,
        )
        self.content = Column(
            controls=[
                # Header
                Row(
                    controls=[
                        Column(
                            controls=[
                                Text(
                                    "Budget Summary",
                                    color="black",
                                    size=30,
                                    weight=FontWeight.BOLD,
                                ),
                                Text("Overview of your monthly budget"),
                            ]
                        )
                    ]
                ),
                Row(
                    controls=[
                        Text(
                            "Total Income",
                            color="black",
                            weight=FontWeight.BOLD,
                        ),
                        self.total_income,
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
                Row(
                    controls=[
                        Text(
                            "Fixed Expenses",
                            color="black",
                            weight=FontWeight.BOLD,
                        ),
                        Text(
                            "-$$$",
                            color="red",
                            weight=FontWeight.BOLD,
                            text_align=TextAlign.RIGHT,
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
                Row(
                    controls=[
                        Text(
                            "Variable Expenses",
                            color="black",
                            weight=FontWeight.BOLD,
                        ),
                        Text(
                            "-$$$",
                            color="red",
                            weight=FontWeight.BOLD,
                            text_align=TextAlign.RIGHT,
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
                # data in
                Divider(),
                Row(
                    controls=[
                        Text(
                            "Total Income",
                            color="black",
                            weight=FontWeight.BOLD,
                        ),
                        Text(
                            "$$$",
                            color="green",
                            weight=FontWeight.BOLD,
                            text_align=TextAlign.RIGHT,
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
        )

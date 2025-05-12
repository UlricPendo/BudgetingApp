from flet import (
    Container,
    Text,
    Colors,
    Column,
    FontWeight,
    Divider,
    Row,
    CrossAxisAlignment,
    MainAxisAlignment,
    TextAlign,
)


class SavingsSummary(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = "white"
        self.height = 300
        self.border_radius = 15
        self.padding = 20
        self.margin = 5
        self.content = Column(
            controls=[
                # Header
                Row(
                    controls=[
                        Column(
                            controls=[
                                Text(
                                    "Savings",
                                    color="black",
                                    size=30,
                                    weight=FontWeight.BOLD,
                                ),
                                Text("Your Savings breakdown"),
                            ]
                        )
                    ]
                ),
                # data in
                Row(
                    controls=[
                        Column(
                            expand=True,
                            controls=[
                                Text(
                                    "Savings Rate",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                                Text(
                                    "Monthyl Savings",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                                Text(
                                    "Total Expanses",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                                Text(
                                    "Expanse Ratio",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                            ],
                        ),
                        # Math part
                        Column(
                            horizontal_alignment=CrossAxisAlignment.END,
                            controls=[
                                Text(
                                    "%%",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                                Text(
                                    "$$$",
                                    color="green",
                                    weight=FontWeight.BOLD,
                                ),
                                Text(
                                    "$$$",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                                Text(
                                    "%%",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

from flet import (
    Container,
    Text,
    Colors,
    Column,
    CrossAxisAlignment,
    FontWeight,
    Row,
    TextAlign,
    Divider,
    Slider,
)


class EmergancyFund(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = "white"
        self.height = 300
        self.border_radius = 15
        self.padding = 10
        self.margin = 10

        def slider_changed(e):
            months.value = f"{e.control.value}"
            self.update()

        months = Text()

        self.content = Column(
            controls=[
                # Header
                Row(
                    controls=[
                        Column(
                            controls=[
                                Text(
                                    "Emergency Fund",
                                    color="black",
                                    size=30,
                                    weight=FontWeight.BOLD,
                                ),
                                Text("Plan for the unexpected expenses"),
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
                                    "Number Of Months To Cover",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                                Slider(
                                    min=0,
                                    max=12,
                                    divisions=12,
                                    label="{value} Months",
                                    on_change=slider_changed,
                                ),
                                Text(
                                    "Fixed Expenses",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                                Text(
                                    "Variable Expenses",
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
                                    months,
                                    color="green",
                                    weight=FontWeight.BOLD,
                                    text_align=TextAlign.RIGHT,
                                ),
                                Text(
                                    "-$$$$",
                                    color="Red",
                                    weight=FontWeight.BOLD,
                                    text_align=TextAlign.RIGHT,
                                ),
                                Text(
                                    "-$$$$$",
                                    color="Red",
                                    weight=FontWeight.BOLD,
                                    text_align=TextAlign.RIGHT,
                                ),
                            ],
                        ),
                    ],
                ),
                Divider(),
                Row(
                    controls=[
                        Column(
                            expand=True,
                            controls=[
                                Text(
                                    "Money Left Over",
                                    color="black",
                                    weight=FontWeight.BOLD,
                                ),
                            ],
                        ),
                        Column(
                            horizontal_alignment=CrossAxisAlignment.END,
                            controls=[
                                Text(
                                    "$$$",
                                    color="green",
                                    weight=FontWeight.BOLD,
                                    text_align=TextAlign.RIGHT,
                                ),
                            ],
                        ),
                    ]
                ),
            ],
        )

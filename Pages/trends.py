from flet import Container, Text, Colors, Column


class Budgettrends(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = "white"
        self.height = 300
        self.border_radius = 15
        self.padding = 10
        self.margin = 10
        self.content = Column([Text("Budget Trends"), Text("yo guy")])

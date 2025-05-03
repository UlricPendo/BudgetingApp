from flet import Container, Text, Colors, Column


class EmergancyFund(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = "white"
        self.width = 300
        self.height = 300
        self.border_radius = 15
        self.padding = 10
        self.margin = 10
        self.content = Column([Text("Emergancy Fund Guy"), Text("yo guy")])

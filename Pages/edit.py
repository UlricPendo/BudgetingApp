from flet import View, Text, ControlEvent, ElevatedButton


class EditView(View):
    def __init__(self, ctrl: Text, *args, **kwargs):
        super().__init__(route="/edit", *args, **kwargs)
        self.bgcolor = "white"
        self.text = ctrl
        self.controls = [
            Text(value=ctrl.value),
            ElevatedButton(text="Discard", on_click=self.save),
        ]

    def save(self, _: ControlEvent) -> None:
        # self.text.value = f"{self.descriptionInput.value} | ${self.income_input.value} | {self.Dateinput.value} "
        self.page.views.pop()
        self.page.update()


# THIS IS SAVEING TO FILE ON UPDATE
# how to parse what you want from string
# values = self.text.value.split(" | ")
# # values[0] is the description this is what goes in line 27
# # load data
# df = pd.read_csv("./income.csv")
# # filter for matching row
# filtered_df = df[(df["Description"] == description) & (df["Amount"] == amount) & (df["Date"] == date)]
# # overwrite
# filtered_df["Description"].iloc[0] = new_description
# filtered_df["Amount"].iloc[0] = new_amount
# filtered_df["Date"].iloc[0] = new_date
# # save
# df.to_csv("./income.csv", index=False)

# FOR REMOVING
# df = pd.read_csv("./income.csv")
# filtered_df = df[(df["Description"] == description) & (df["Amount"] == amount) & (df["Date"] == date)]
# df.drop(filtered_df.iloc[0].index)
# df.to_csv("./income.csv", index=False)

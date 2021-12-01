from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
# from kivy.core.window import Window

# Window.size = (300, 600)

Builder.load_file("design.kv")


class MainWidget(Widget):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)

    def clear(self):
        self.ids.input_calc.text = "="
        self.ids.input_show.text = "0"

    def backspace(self):
        memo = self.ids.input_show.text
        memo = memo[:-1]
        self.ids.input_show.text = memo

    def plus_minus(self):

        if str(self.ids.input_show.text).startswith("-"):
            self.ids.input_show.text = self.ids.input_show.text[1:]
            self.ids.input_calc.text = str(eval(self.ids.input_show.text))
        else:
            self.ids.input_show.text = "-" + self.ids.input_show.text
            self.ids.input_calc.text = str(eval(self.ids.input_show.text))

    def insert_value(self, val):

        # Inserting values in Show
        if self.ids.input_show.text == "0":
            self.ids.input_show.text = ""
            self.ids.input_show.text = str(val)

        else:
            memo = self.ids.input_show.text
            self.ids.input_show.text = ""
            self.ids.input_show.text = memo + str(val)

        # Showing result on output
        try:
            memo = str(self.ids.input_show.text)
            if "%" in memo:
                memo = str(eval(memo.rstrip("%"))/100)
                self.ids.input_calc.text = memo
            else:
                self.ids.input_calc.text = str(eval(memo.rstrip("+-*/")))
        except SyntaxError:
            self.ids.input_show.text = "Invalid Input!"
            self.ids.input_calc.text = ":("

    def equal(self):
        try:
            self.ids.input_show.text = self.ids.input_calc.text
            self.ids.input_calc.text = "="

        except SyntaxError:
            self.ids.input_calc.text = "Error"


class Calculator(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    Calculator().run()

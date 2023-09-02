from datetime import datetime

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, DictProperty

from viewmodels import data_access as da
from structures.food import Meal


class LabelTextInput(BoxLayout):

    def __init__(self, name, **kwargs):
        self.name = name
        super(LabelTextInput, self).__init__(**kwargs)
        self.ids.text = name

class MenuLayout(BoxLayout):
    ...


class DayLine(BoxLayout):

    def __init__(self, value: dict, **kwargs):
        self.value = value
        super(DayLine, self).__init__(**kwargs)


class MainActivity(BoxLayout):
    def show_data(self, diary: list):
        for data in diary:
            value: dict
            self.ids.body.add_widget(DayLine(data))


class BottomLayout(BoxLayout):
    ...


class AddMealScreen(BoxLayout):
    """role should be meal or ...."""
    body = ObjectProperty()
    def __init__(self, role: str, container: dict, **kwargs):
        super(AddMealScreen, self).__init__(**kwargs)
        self.role = role
        self.container = container
        self.add_line()

    def add_line(self):
        self.body.add_widget(LabelTextInput("Название"))

    def save(self):
        if self.role == "meal":
            for line in self.body.children:
                value = line.ids.name.text
                if not value:
                    continue
                quant = line.ids.quant.text
                if quant and not quant.isnumeric():
                    raise ValueError(f"Неверно значение количества для {value}")
                self.container[value] = quant
        if not self.container:
            return
        acc = da.DataAccess()
        acc.add_meal(self.container, datetime.now())


class RTextInput(TextInput):
    ...



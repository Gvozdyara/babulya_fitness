from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, DictProperty


class LabelTextInput(BoxLayout):

    def __init__(self, name, **kwargs):
        super(BoxLayout, self).__init__(**kwargs)
        self.ids.text = name

class MenuLayout(BoxLayout):
    ...


class MainActivity(Screen):
    ...


class BottomLayout(BoxLayout):
    ...


class AddMealScreen(Screen):
    body = ObjectProperty()
    def __init__(self, role: str, container: dict, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.role = role
        self.container = container
    def add_line(self):
        self.body.add_widget(LabelTextInput("Название"))

    def save(self):
        if self.role == "meal":
            for line in self.body.children:
                value = line.ids.text.text
                if not value:
                    continue
                quant = line.ids.quant.text
                if quant and not quant.isnumeric():
                    raise ValueError(f"Неверно значение количества для {value}")
                self.container[value] = quant




class RTextInput(TextInput):
    ...



from datetime import datetime

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, DictProperty, StringProperty
from kivy.clock import Clock

from viewmodels.data_access import DA
from structures.food import Meal


class AddFoodLine(BoxLayout):

    def __init__(self, **kwargs):
        super(AddFoodLine, self).__init__(**kwargs)
        self.event = None

    def show_food_name_hint(self, chunk: str):
        self.get_food_names(chunk)

    def get_food_names(self, chunk: str):
        if self.event is not None:
            self.event.cancel()

        self.event = Clock.schedule_once(lambda dt: DA.filter_food_names(chunk), 0.8)



class LabelTextInput(BoxLayout):

    name_value = StringProperty()
    name_label = ObjectProperty()

    def __init__(self, name="", **kwargs):
        self.name = name
        super(LabelTextInput, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: setattr(self.name_label, "text", name), 0.1)


class NameHintsBox(RecycleView):

    def __init__(self, data: list, name_holder: LabelTextInput, **kwargs):
        self.data = [{"text": i, "parent_": self, "name_holder": name_holder} for i in self.data]
        super().__init__(NameHintsBox, self).__init__(**kwargs)

class NameHintButton(Button):

    def __init__(self, name_holder : TextInput, parent_: NameHintsBox, **kwargs):
        self.name_holder = name_holder
        self.parent_ = parent_
        super().__init__(**kwargs)

    def on_release(self):
        self.name_holder.ids.name.ids.name = self.text
        self.parent_.data.clear()



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
        self.body.add_widget(AddFoodLine())

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


class RTextInput(TextInput):
    ...



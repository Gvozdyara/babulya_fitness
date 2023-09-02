from datetime import datetime
from random import randint

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui import widgets
from kivy.properties import ObjectProperty

import constants as cnst
from viewmodels.main_activity_vm import MainActivityVM
from ui.widgets import AddMealScreen


class MainLayout(BoxLayout):
    main_activity: BoxLayout = ObjectProperty()
    def __init__(self, main_activity_vm: MainActivityVM, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.fake_content()

    def show_add_meal_screen(self):
        self.main_activity.ids.body.clear_widgets()
        self.main_activity.ids.body.add_widget(AddMealScreen("meal", {}))

    def fake_content(self):
        dic = []

        for i in reversed(range(1, 30)):
            data = {
                "date": f'{cnst.WEEK_DAYS[datetime(2023, 8, i).weekday()]} {datetime(2023, 8, i).strftime("%d.%m.%Y")}',
                "proteins": str(randint(0, 20)),
                "fats": str(randint(0, 20)),
                "carboh": str(randint(0, 60)),
                "calories": str(randint(0, 1000)),
            }
            dic.append(data)
        self.ids.main_activity.show_data(dic)
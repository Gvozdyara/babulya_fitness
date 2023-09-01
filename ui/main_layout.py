from datetime import datetime
from random import randint

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui import widgets
from kivy.properties import ObjectProperty


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.fake_content()

    def fake_content(self):
        dic = []

        for i in reversed(range(1, 30)):
            data = {
                "date": datetime(2023, 8, i).isoformat(),
                "proteins": str(randint(0, 20)),
                "fats": str(randint(0, 20)),
                "carboh": str(randint(0, 60)),
                "calories": str(randint(0, 1000)),

            }
            dic.append(data)
        self.ids.main_activity.show_data(dic)

from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '700')
from kivy.app import App

from ui.main_layout import MainLayout
from viewmodels.main_activity_vm import MainActivityVM




class MainApp(App):

    def __init__(self, **kwargs):
        self.main_activity_vm = MainActivityVM()
        super().__init__(**kwargs)


    def build(self):
        return MainLayout(self.main_activity_vm)
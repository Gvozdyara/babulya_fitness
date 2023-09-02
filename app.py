
from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '700')
from kivy.app import App
from ui.main_layout import MainLayout




class MainApp(App):

    def build(self):
        return MainLayout()
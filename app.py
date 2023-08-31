from kivy.app import App
from ui.main_layout import MainLayout




class MainApp(App):

    def build(self):
        return MainLayout()
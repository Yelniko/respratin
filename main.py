from kivy.uix.screenmanager import ScreenManager
from settings import Settings
from window_1 import Window1
from window_2 import Window2
from kivy.app import App


class Respiration_App(App):
    def build(self):
        mu = ScreenManager()

        mu.add_widget(Window1())
        mu.add_widget(Window2())
        mu.add_widget(Settings())

        return mu


if __name__ == '__main__':
    Respiration_App().run()

from window_customisable_triangle_1 import Window1
from window_customisable_triangle_2 import Window2
from kivy.uix.screenmanager import ScreenManager
from window_first import WindowFirst
from settings import Settings
from kivy.app import App


class Respiration_App(App):
    def build(self):
        mu = ScreenManager()

        mu.add_widget(WindowFirst())
        mu.add_widget(Settings())
        mu.add_widget(Window1())
        mu.add_widget(Window2())

        return mu


if __name__ == '__main__':
    Respiration_App().run()

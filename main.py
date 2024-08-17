from window_customisable_triangle_1 import WindowCT1
from window_customisable_triangle_2 import WindowCT2
from kivy.uix.screenmanager import ScreenManager
from window_breath_holding_1 import WindowBH1
from window_breath_holding_2 import WindowBH2
from window_breathing import WindowB
from window_first import WindowFirst
from window_triangle import WindowT
from window_square import WindowQ
from settings import Settings
from kivy.app import App


class Respiration_App(App):
    def build(self):
        mu = ScreenManager()

        mu.add_widget(WindowFirst())
        mu.add_widget(Settings())
        mu.add_widget(WindowB())
        mu.add_widget(WindowQ())
        mu.add_widget(WindowT())
        mu.add_widget(WindowCT1())
        mu.add_widget(WindowCT2())
        mu.add_widget(WindowBH1())
        mu.add_widget(WindowBH2())

        return mu


if __name__ == '__main__':
    Respiration_App().run()

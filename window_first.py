from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class WindowFirst(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)

        lent = BoxLayout(orientation='vertical', padding=10)

        lent.add_widget(Label(text='Choose a breathing technique', font_size='60'))
        lent.add_widget(Button(text='Breathing', font_size='60', on_press=self.breathing))
        lent.add_widget(Button(text='Square', font_size='60', on_press=self.square))
        lent.add_widget(Button(text='Triangle', font_size='60', on_press=self.triangle))
        lent.add_widget(Button(text='Customisable triangle', font_size='60', on_press=self.customisable_triangle))
        lent.add_widget(Button(text='Breath-holding', font_size='60', on_press=self.breath_holding))
        lent.add_widget(Button(text='Settings', font_size='60', on_press=self.settings))

        self.add_widget(lent)

    def breathing(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'window_breathing'

    def square(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'window_square'

    def triangle(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'window_triangle'

    def customisable_triangle(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'window_customisable_triangle_1'

    def breath_holding(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'window_breath-holding_1'

    def settings(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'settings'
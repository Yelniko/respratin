from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class Settings(Screen):
    def __init__(self, name='settings'):
        super().__init__(name=name)

        with open('settings_memory.txt', 'r') as file1:
            self.settings = list(map(int, file1.read().split()))

        self.music_condition = 'Music ON'

        if self.settings[1] == 0:
            self.music_condition = 'Music OFF'

        lent = BoxLayout(orientation='vertical', padding=10)
        self.music_button = Button(text=self.music_condition, font_size='20', on_press=self.music)

        lent.add_widget(self.music_button)
        lent.add_widget(Button(text='Exit', font_size='20', on_press=App.get_running_app().stop))
        lent.add_widget(Button(text='Back', font_size='20', on_press=self.back))

        self.add_widget(lent)

    def music(self, instance):
        if instance.text == 'Music ON':
            self.settings[1] = 0
            self.music_button.text = 'Music OFF'
        else:
            self.settings[1] = 1
            self.music_button.text = 'Music ON'

    def back(self, instance):
        with open('settings_memory.txt', 'w') as file1:
            file1.write(f'{self.settings[0]} {self.settings[1]}')
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'

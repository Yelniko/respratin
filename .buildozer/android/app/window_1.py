from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label




class Window1(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)

        with open('settings_memory.txt', 'r') as file1:
            self.second = list(map(int, file1.read().split()))

        self.lab = Label(text=str(self.second[0]), font_size=140)
        self.button = Button(text='Settings', on_press=self.settings)
        self.button_1 = Button(text='Next', on_press=self.next)

        self.button.size_hint_y = 0.8
        self.button_1.size_hint_y = 0.8

        lent = BoxLayout(orientation='vertical', padding=10)
        lent_1 = BoxLayout(padding=2)
        lent.add_widget(Button(text='+', font_size=140, background_color='#000000', on_press=self.enter))
        lent.add_widget(self.lab)
        lent.add_widget(Button(text='-', font_size=140, background_color='#000000', on_press=self.enter))
        lent_1.add_widget(self.button)
        lent_1.add_widget(self.button_1)
        lent.add_widget(lent_1)

        self.add_widget(lent)

    def enter(self, instance):
        if instance.text == '+':
            self.lab.text = str(int(self.lab.text)+1)
        else:
            if int(self.lab.text) > 3:
                self.lab.text = str(int(self.lab.text)-1)

    def next(self, instance):
        with open('settings_memory.txt', 'r') as file1:
            self.second = list(map(int, file1.read().split()))
        with open('settings_memory.txt', 'w') as file1:
            file1.write(f'{self.lab.text} {self.second[1]}')
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

    def settings(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'settings'

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


class WindowBH2(Screen):
    def __init__(self, name='window_breath-holding_2'):
        super().__init__(name=name)

        with open('breath-holding_memory.txt', 'r') as file1:
            self.memory = list(map(int, file1.read().split()))

        self.seconds = 0

        self.lab = Label(text='0 : 00', font_size=140)
        self.but = Button(text='Start', on_press=self.start_stop, font_size=100)

        lent = BoxLayout(orientation='vertical', padding=2)
        lent_b = BoxLayout(padding=2)

        lent_b.add_widget(Button(text='Back', on_press=self.back, font_size=100))
        lent_b.add_widget(self.but)

        lent.add_widget(self.lab)
        lent.add_widget(lent_b)

        self.add_widget(lent)

    def start_stop(self, instance):
        if instance.text == 'Start' or instance.text == 'Restart':
            self.lab.text = '0 : 00'
            self.but.text = 'Stop'
            self.cl = Clock.schedule_interval(self.tim, 1)
        else:
            self.cl.cancel()
            self.but.text = 'Restart'
            with open('breath-holding_memory.txt', 'a') as file1:
                file1.write(f' {self.seconds}')

    def tim(self, df):
        self.seconds += 1
        self.lab.text = f'{self.seconds // 60} : {(self.seconds % 60):02}'

    def back(self, instance):
        self.but.text = 'Stop'
        self.manager.transition.direction = 'right'
        self.manager.current = 'window_breath-holding_1'

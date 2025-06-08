from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


class WindowBH1(Screen):
    def __init__(self, name='window_breath-holding_1'):
        super().__init__(name=name)

        with open('breath-holding_memory.txt', 'r') as file1:
            self.memory = list(map(int, file1.read().split()))

        self.lad_1 = Label(text=f'{self.memory[-1] // 60} : {(self.memory[-1] % 60):02}', font_size=65)
        self.lad_2 = Label(text=f'{(int(sum(self.memory)/len(self.memory))) // 60} : {((int(sum(self.memory) / len(self.memory))) % 60):02}', font_size=65)
        self.lad_3 = Label(text=f'{max(self.memory)// 60} : {(max(self.memory) % 60):02}', font_size=65)

        lent = BoxLayout(orientation='vertical', padding=2)
        lent_text_1 = BoxLayout(orientation='vertical', padding=2)
        lent_text_2 = BoxLayout(orientation='vertical', padding=2)
        lent_text_3 = BoxLayout(orientation='vertical', padding=2)
        lent_1 = BoxLayout(padding=3)
        lent_b = BoxLayout(padding = 2)

        lent_text_1.add_widget(Label(text='Recent', font_size=65))
        lent_text_1.add_widget(self.lad_1)

        lent_text_2.add_widget(Label(text='Average', font_size=65))
        lent_text_2.add_widget(self.lad_2)

        lent_text_3.add_widget(Label(text='Max', font_size=65))
        lent_text_3.add_widget(self.lad_3)

        lent_b.add_widget(Button(text='Back', on_press=self.back, font_size=100))
        lent_b.add_widget(Button(text='Test', on_press=self.test, font_size=100))

        lent_1.add_widget(lent_text_1)
        lent_1.add_widget(lent_text_2)
        lent_1.add_widget(lent_text_3)

        lent.add_widget(lent_1)
        lent.add_widget(lent_b)

        self.add_widget(lent)

    def update(self, df):
        with open('breath-holding_memory.txt', 'r') as file1:
            self.memory = list(map(int, file1.read().split()))
        self.lad_1.text = f'{self.memory[-1] // 60} : {(self.memory[-1] % 60):02}'
        self.lad_2.text = f'{(int(sum(self.memory)/len(self.memory))) // 60} : {((int(sum(self.memory) / len(self.memory))) % 60):02}'
        self.lad_3.text = f'{max(self.memory)// 60} : {(max(self.memory) % 60) :02}'

    def test(self, instance):
        self.cl = Clock.schedule_interval(self.update, 1)
        self.manager.transition.direction = 'left'
        self.manager.current = 'window_breath-holding_2'

    def back(self, instance):
        if hasattr(self, 'cl'):
            self.cl.cancel()
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.label import Label
from functools import partial
from kivy.clock import Clock


class Window2(Screen):
    def __init__(self, name='window_customisable_triangle_2'):
        super().__init__(name=name)

        self.value = 0
        self.second = 4
        self.lab_1_text = 'Breath'
        self.lab_2_text = 'Hold your breath'
        self.lab_3_text = 'Exhalation'
        self.music = SoundLoader.load('music/chasyi-tikane-sekundomera-versiya-2-24139.mp3')
        self.music_1 = SoundLoader.load('music/zvon-v-korabelnyiy-kolokol-37902.mp3')
        self.music.loop = True
        self.config = []

        lent = BoxLayout(orientation='vertical', padding=10)
        lent_1 = BoxLayout(padding=2)
        self.meter = Label(text='0', font_size=140)
        self.bar_1 = ProgressBar(value=self.value, max=self.second, size_hint_y=None, height=40)
        self.bar_2 = ProgressBar(value=self.value, max=self.second * 4, height=100)
        self.bar_3 = ProgressBar(value=self.value, max=self.second * 2, height=100)
        self.but = Button(text='Start', on_press=self.start_stop, font_size=20)
        self.bar_1_lab_1 = Label(text=self.lab_1_text, font_size=80)
        self.bar_2_lab_2 = Label(text=self.lab_2_text, font_size=80)
        self.bar_3_lab_3 = Label(text=self.lab_3_text, font_size=80)

        lent.add_widget(self.meter)
        lent.add_widget(self.bar_1_lab_1)
        lent.add_widget(self.bar_1)
        lent.add_widget(self.bar_2_lab_2)
        lent.add_widget(self.bar_2)
        lent.add_widget(self.bar_3_lab_3)
        lent.add_widget(self.bar_3)
        lent_1.add_widget(Button(text='Back', on_press=self.back, font_size=20))
        lent_1.add_widget(self.but)
        lent.add_widget(lent_1)

        self.add_widget(lent)

    def start(self):
        with open('settings_memory.txt', 'r') as file1:
            self.config = list(map(int, file1.read().split()))
        self.bar_1.max = self.config[0]
        self.bar_2.max = self.config[0] * 4
        self.bar_3.max = self.config[0] * 2

    def start_stop(self, instance):
        self.start()
        if instance.text == 'Start' or instance.text == 'Restart':
            if self.config[1] == 1:
                self.music.play()
                self.cl_music_1 = Clock.schedule_interval(self.music_fan, self.config[0]-1)

            self.meter.text = '0'
            self.but.text = 'Stop'
            self.timer()
            self.cl_4 = Clock.schedule_interval(self.tim, self.config[0] + self.config[0] * 2 + self.config[0] * 4)
        else:
            self.music.stop()
            self.cl_music_1.cancel()
            try:
                self.cl_1.cancel()
                self.bar_1.value = 0
                self.bar_1_lab_1.text = self.lab_1_text
                self.cl_1_lab_1.cancel()
            except:
                pass
            try:
                self.cl_2.cancel()
                self.bar_2.value = 0
                self.bar_2_lab_2.text = self.lab_2_text
                self.cl_2_lab_2.cancel()
            except:
                pass
            try:
                self.cl_3.cancel()
                self.bar_3.value = 0
                self.bar_3_lab_3.text = self.lab_3_text
                self.cl_3_lab_3.cancel()
            except:
                pass
            try:
                self.cl_4.cancel()
            except:
                pass

            self.but.text = 'Restart'

    def timer(self):
        self.bar_1_lab_1.text = f'{self.lab_1_text}: {self.config[0]}'
        self.bar_2_lab_2.text = f'{self.lab_2_text}: {self.config[0] * 4}'
        self.bar_3_lab_3.text = f'{self.lab_3_text}: {self.config[0] * 2}'
        self.bar_1.value = 0.1

        self.cl_1 = Clock.schedule_interval(partial(self.bar_prog, [self.config[0], self.bar_1]), 0.1)
        self.cl_1_lab_1 = Clock.schedule_interval(partial(self.leb_prog, self.bar_1_lab_1), 1)
        self.cl_2 = Clock.schedule_interval(self.cl_2_1, self.config[0])
        self.cl_3 = Clock.schedule_interval(self.cl_3_1, self.config[0] + self.config[0] * 4)

    def tim(self, df):
        self.meter.text = str(int(self.meter.text)+1)

    def music_fan(self, df):
        self.music_1.play()
        self.cl_music_1.cancel()
        self.cl_music_1 = Clock.schedule_interval(self.music_fan_1, self.config[0] * 4)

    def music_fan_1(self, df):
        self.music_1.play()
        self.cl_music_1.cancel()
        self.cl_music_1 = Clock.schedule_interval(self.music_fan_2, self.config[0] * 2)

    def music_fan_2(self, df):
        self.music_1.play()
        self.cl_music_1.cancel()
        self.cl_music_1 = Clock.schedule_interval(self.music_fan, self.config[0])

    def bar_prog(self, lis, *largs):
        if lis[1].value < lis[0]:
            lis[1].value += 0.1

    def leb_prog(self, lis, *largs):
        number = list(lis.text.split(': '))
        if int(number[1]) > 0:
            lis.text = f'{number[0]}: {int(number[1])-1}'

    def cl_1_1(self, df):
        self.bar_3.value = 0
        self.cl_3.cancel()
        self.cl_3_lab_3.cancel()
        self.bar_3_lab_3.text = f'{self.lab_3_text}: 0'
        self.cl_1.cancel()
        self.timer()

    def cl_2_1(self, df):
        self.cl_1.cancel()
        self.cl_1_lab_1.cancel()
        self.bar_1_lab_1.text = f'{self.lab_1_text}: 0'
        self.bar_1.value = 0
        self.cl_2.cancel()
        self.bar_2.value = 0.1
        self.cl_2_lab_2 = Clock.schedule_interval(partial(self.leb_prog, self.bar_2_lab_2), 1)
        self.cl_2 = Clock.schedule_interval(partial(self.bar_prog, [self.config[0] * 4, self.bar_2]), 0.1)

    def cl_3_1(self, df):
        self.cl_2.cancel()
        self.cl_2_lab_2.cancel()
        self.bar_2_lab_2.text = f'{self.lab_2_text}: 0'
        self.bar_2.value = 0
        self.cl_3.cancel()
        self.bar_3.value = 0.1
        self.cl_3_lab_3 = Clock.schedule_interval(partial(self.leb_prog, self.bar_3_lab_3), 1)
        self.cl_3 = Clock.schedule_interval(partial(self.bar_prog, [self.config[0] * 2, self.bar_3]), 0.1)
        self.cl_1 = Clock.schedule_interval(self.cl_1_1, self.config[0] * 2)

    def back(self, instance):
        if self.but.text == 'Stop':
            self.start_stop(self.but)
        self.but.text = 'Start'
        self.meter.text = '0'
        self.manager.transition.direction = 'right'
        self.manager.current = 'window_customisable_triangle_1'

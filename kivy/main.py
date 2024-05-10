from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

from kivy.core.window import Window
Window.size = (375, 650)



class MainMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        axis = BoxLayout(
            orientation = 'vertical',
            padding = (50, 150, 50, 150),
            spacing = 10
        )
        # кнопки пменю
        calc_btn = Button(
            text = 'Калькулятор',
            font_size = 18,
            on_press = self.switch_to_second
        )
        axis.add_widget(calc_btn)


        conv_btn = Button(
            text = 'Конвертер',
            font_size = 18,
            on_press = self.switch_to_second
        )
        axis.add_widget(conv_btn)

        timer_btn = Button(
            text = 'Таймер',
            font_size = 18,
            on_press = self.switch_to_second
        )
        axis.add_widget(timer_btn)
        stopwatch_btn = Button(
            text = 'Секундомер',
            font_size = 18,
            on_press = self.switch_to_second
        )
        axis.add_widget(stopwatch_btn)

        self.add_widget(axis)
#======================================================================================       

    def switch_to_second(self, instance):
        screens = {
            'Калькулятор' : 'calculator',
            'Конвертер' : 'converter',
            'Таймер' : 'timer',
            'Секундомер' : 'stopwatch'
        }
        self.manager.transition.direction = 'left'
        self.manager.current = screens[instance.text]

class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = BoxLayout()

        back_btn = Button(
            text = 'Назад :)',
            size_hint = (None, None),
            size = (100, 50,),
            font_size = 18,
            pos_hint = {'top': 1.0, 'x': 0.0},
            on_press = self.switch_to_main
        )

        self.layout.add_widget(back_btn)

        self.add_widget(self.layout)

    def switch_to_main(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_menu'

class CalcScreen(SecondScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        axis = BoxLayout(
            orientation = 'vertical',
            padding = (50, 150, 50, 150)
        )

        self.result = Label(
            text = '0',
            size_hint_y = None,
            height = 100,
            font_size = 32
        )
        axis.add_widget(self.result)

        keyboard = GridLayout(cols = 4)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for b in buttons:
            temp = Button(
                text = b,
                font_size = 26,
                on_press = self.keyboard_press
            )
            keyboard.add_widget(temp)

        axis.add_widget(keyboard)

        self.add_widget(axis)
    
    def keyboard_press(self, instance):
        current = self.result.text
        btn = instance.text

        if current == '0' or current == 'Ошибка ало':
            self.result.text = ''
            current = ''

        if btn == '=':
            try:
                self.result.text = str(eval(current))
            except:
                self.result.text = 'Ошибка ало'
        elif btn == 'C':
            self.result.text = '0'
        else:
            self.result.text = current + btn


class ConvScreen(SecondScreen):
    pass

class TimerScreen(SecondScreen):
    pass

class StopwatchScreen(SecondScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.time = 0
        self.run = False

        axis = BoxLayout(
            orientation = 'vertical',
            spacing = 10,
            padding = (50, 150, 50, 150)
        )

        self.label = Label(
            text = '00:00:00',
            font_size = 32,
        )
        axis.add_widget(self.label)

        self.start_btn = Button(
            text = 'Запуск',
            font_size = 32,
            size_hint = (None, None),
            size = (200, 50),
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            on_press = self.start_stop
        )
        axis.add_widget(self.start_btn)

        self.reset_btn = Button(
            text = 'Сбросить',
            font_size = 32,
            size_hint = (None, None),
            size = (200, 50),
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            on_press = self.reset
        )
        axis.add_widget(self.reset_btn)

        self.add_widget(axis)


        Clock.schedule_interval(self.update_time, 0.01)

    def start_stop(self, instance):
        self.run = not self.run
        if self.run:
            self.start_btn.text = 'Пауза'
        else:
            self.start_btn.text = 'Запуск'

    def reset(self, instance):
        self.run = False
        self.time = 0
        self.label.text = '00:00:00'
        self.start_btn.text = 'Запуск'
    
    def format_time(self, ms):
        s, ms = divmod(ms, 100)
        m, s = divmod(s, 60)
        return f'{m:02}:{s:02}:{ms:02}'

    def update_time(self, dt):
        if self.run:
            self.time += 1
        self.label.text = self.format_time(self.time)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name = 'main_menu'))
        sm.add_widget(CalcScreen(name = 'calculator'))
        sm.add_widget(ConvScreen(name = 'converter'))
        sm.add_widget(TimerScreen(name = 'timer'))
        sm.add_widget(StopwatchScreen(name = 'stopwatch'))
        return sm




app = MyApp()
app.run()
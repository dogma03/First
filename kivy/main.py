from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

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
    pass

class ConvScreen(SecondScreen):
    pass

class TimerScreen(SecondScreen):
    pass

class StopwatchScreen(SecondScreen):
    pass


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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QListWidget, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt

# -----------------создание приложения и работа с окном-----------------------
app = QApplication([]) # выделение места и создание приложения

game = QWidget() # создание окна
game.resize(600, 600)
game.setWindowTitle('Игра')
game.show() # по умолчанию окно скрыто и нужно его показать

# ---------------------------визуальная часть приложения-----------------------

# создание направляющих
v_line = QVBoxLayout()
h_line = QHBoxLayout()
low_line = QHBoxLayout()

inventory = QListWidget() # Ну игровая область там текст инвентарь и сё такое
information = QTextEdit()
information.setReadOnly(True)
btn1 = QPushButton('Использовать') # кнопки
btn2 = QPushButton('Защита') # ➡️➡️⬆️
btn3 = QPushButton('Удар') # ➡️➡️➡️➡️⬆️

h_line.addWidget(inventory) # добалвление всяких панелек
h_line.addWidget(information) # ⬆️

v_line.addLayout(h_line)  # закрепление горизонтальной линии на вертикальной направляющей

low_line.addWidget(btn1) # добавление кнопырей
low_line.addWidget(btn2) # ⬆️
low_line.addWidget(btn3) # ⬆️

v_line.addLayout(low_line)

game.setLayout(v_line) # закрепление основного лэйаута для окна

#------------------------------Классы--------------------------------------------------------

class Character():
    def __init__(self, name, hp, armor, power, inventory=[]):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.inventory = inventory
    def print_info(self):
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}')
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}')
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}\nУровень брони: {self.armor}')
        information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПоприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}\nУровень брони: {self.armor}\nСила удара: {self.power}')
    def strike(self, enemy):
        enemy.armor -= self.power
        if enemy.armor <= 0:
            enemy.hp += enemy.armor
            enemy.armor = 0

#===================================Функции и всё такое===========================================

def new():
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире')
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории')
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории\nПо сюжету ты обычный торговец, но гуляя как-то раз по лесу, ты находишь меч, и решаешь встать на путь путешественника')
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории\nПо сюжету ты обычный торговец, но гуляя как-то раз по лесу, ты находишь меч, и решаешь встать на путь путешественника\nНажми кнопку использовать чтобы начать игру')


def new_walk():
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nВы решили пройтись по лесу и заметили странно здание, желаете войти?')
    btn2 = QPushButton('Войти в дом')
    find_potion = f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nЗайдя в дом вы нашли 3 странных зелья, красное, зелёное и синее, рядом с ними была книга с описанием зелий, какую вы хотите прочесть первой?'
    btn2.clicked.connect(find_potion)
    btn1 = QPushButton('Красное зелье')
    btn1 = QPushButton('Зелёное зелье')
    btn1 = QPushButton('Синее зелье')
    btn1.clicked.connect(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nОписание: "Красное зелье увеличивает ваш урон на 3 хода в течении одного боя на 50%"')
    btn2.clicked.connect(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nОписание: "Зелёное зелье повышает вашу защиту на 3 хода в течении одного матча на 50%"')
    btn3.clicked.connect(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nОписание: "Синее зелье повышает ваш уровень здоровья на 3 хода в течении одного матча на 50%')

    btn1 = QPushButton('Использовать')
    btn2 = QPushButton('Защита')
    btn3 = QPushButton('Удар')

#--------------------------------------------------------------------------------


b_slime = Character('Синий слайм', 25, 5, 5)
g_slime = Character('Зелёный слайм', 35, 0, 45)
goblin = Character('Гоблин', 100, 50, 25)



new()
btn1.clicked.connect(new_walk)



app.exec_()
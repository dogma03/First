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

inventory = QListWidget()
information = QTextEdit()
information.setReadOnly(True)
btn1 = QPushButton('Использовать')
btn2 = QPushButton('Защита')
btn3 = QPushButton('Удар')

h_line.addWidget(inventory)
h_line.addWidget(information)

v_line.addLayout(h_line)

low_line.addWidget(btn1)
low_line.addWidget(btn2)
low_line.addWidget(btn3)

v_line.addLayout(low_line)

# закрепление горизонтальной линии на вертикальной направляющей

# закрепление основного лэйаута для окна
game.setLayout(v_line)

#-------------------------------------------------------------------------------

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

def new():
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире')
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории')
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории\nПо сюжету ты обычный торговец, но гуляя как-то раз по лесу, ты находишь меч, и решаешь встать на путь путешественника')
    information.setText(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\nПривет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории\nПо сюжету ты обычный торговец, но гуляя как-то раз по лесу, ты находишь меч, и решаешь встать на путь путешественника\nНажми кнопку использовать чтобы начать игру')

#--------------------------------------------------------------------------------


b_slime = Character('Синий слайм', 25, 5, 5)
goblin = Character('Гоблин', 100, 50, 25)


btn3.clicked.connect(goblin.print_info)


app.exec_()
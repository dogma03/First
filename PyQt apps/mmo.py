from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QListWidget, QTextEdit
from PyQt5.QtCore import Qt

# -----------------создание приложения и работа с окном-----------------------
app = QApplication([]) # выделение места и создание приложения

game = QWidget() # создание окна
game.resize(300, 300)
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
        information('\n\n\nПоприветствуйте героя ->', self.name)
        information('Уровень здоровья:', self.hp)
        information('Уровень брони:', self.armor)
        information('Сила удара:', self.power)
    def strike(self, enemy):
        enemy.armor -= self.power
        if enemy.armor <= 0:
            enemy.hp += enemy.armor
            enemy.armor = 0

goblin = Character('Гоблин', 100, 50, 25)

btn3.clicked.connect(goblin.print_info)


app.exec_()
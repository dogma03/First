from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QListWidget
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

inventory = QListWidget()
window = QListWidget()
btn1 = QPushButton()
btn2 = QPushButton()
btn3 = QPushButton()
btn4 = QPushButton()
btn5 = QPushButton()

v_line.addWidget(inventory)
v_line.addWidget(window)

v_line.addWidget(btn1)
v_line.addWidget(btn2)
v_line.addWidget(btn3)
v_line.addWidget(btn4)
v_line.addWidget(btn5)

# закрепление горизонтальной линии на вертикальной направляющей
v_line.addLayout(h_line)

# закрепление основного лэйаута для окна
game.setLayout(v_line)

app.exec_()
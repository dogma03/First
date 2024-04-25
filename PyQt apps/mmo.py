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
btn1 = QPushButton()
btn2 = QPushButton()
btn3 = QPushButton()
btn4 = QPushButton()
btn5 = QPushButton()

h_line.addWidget(inventory)
h_line.addWidget(information)

v_line.addLayout(h_line)

low_line.addWidget(btn1)
low_line.addWidget(btn2)
low_line.addWidget(btn3)
low_line.addWidget(btn4)
low_line.addWidget(btn5)

v_line.addLayout(low_line)

# закрепление горизонтальной линии на вертикальной направляющей

# закрепление основного лэйаута для окна
game.setLayout(v_line)

app.exec_()
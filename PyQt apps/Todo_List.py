from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget, QLineEdit
from PyQt5.QtCore import Qt

app = QApplication([]) # выделение места и создание приложения

window = QWidget() # создание окна
window.resize(300, 300)
window.setWindowTitle('Todo List')
window.show() # по умолчанию окно скрыто и нужно его показать

v_line = QVBoxLayout()
h_line = QHBoxLayout()

addB = QPushButton('Добавить')
remB = QPushButton('Удалить')
list = QListWidget()
line = QLineEdit('Новая задача')

v_line.addWidget(list)
v_line.addWidget(line)
h_line.addWidget(addB)
h_line.addWidget(remB)

v_line.addLayout(h_line)

window.setLayout(v_line)

app.exec_()
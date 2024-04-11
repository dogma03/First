from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

# -----------------создание приложения и работа с окном-----------------------
app = QApplication([]) # выделение места и создание приложения

window = QWidget() # создание окна
window.resize(300, 300)
window.setWindowTitle('ПРограмма')
window.show() # по умолчанию окно скрыто и нужно его показать

# ---------------------------визуальная часть приложения-----------------------

# создание направляющих
v_line = QVBoxLayout()
h_line = QHBoxLayout()

# создание виджетов
text = QLabel('Привет, Егор')
btn1 = QPushButton('Нажми 1')
btn2 = QPushButton('Нажми 2')

# закрепление виджетов кнопок на горизонтальной направляющей
h_line.addWidget(btn1, alignment=Qt.AlignCenter)
h_line.addWidget(btn2, alignment=Qt.AlignCenter)

# закрепление виджета текста на вертикальной направляющей
v_line.addWidget(text, alignment=Qt.AlignCenter)
# закрепление горизонтальной линии на вертикальной направляющей
v_line.addLayout(h_line)

# закрепление основного лэйаута для окна
window.setLayout(v_line)

# ==============================ФУНКЦИОНАЛ===================================

# создание функции
def goodbye():
    text.setText('Пока, Егор')


# подключение функции на кнопку
btn2.clicked.connect(goodbye)


app.exec() # выполнение приложения
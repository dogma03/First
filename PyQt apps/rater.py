from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QCheckBox
import string
import random

app = QApplication([])

window = QWidget()
window.resize(300, 300)
window.setWindowTitle('Генератор паролей')
window.show()

v_line= QVBoxLayout()

input_pass = QLabel('vvedi zhivo')
rating = QLabel('Rated')
stroke = QLineEdit()
rater = QPushButton('otsenja')

v_line.addWidget(input_pass)
v_line.addWidget(stroke)
v_line.addWidget(rating)
v_line.addWidget(rater)


window.setLayout(v_line)

app.exec_()
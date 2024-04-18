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

def rate():
    password = stroke.text()
    len_enough = len(password) > 8
    has_uppercase = False
    has_lowercase = False
    has_numbers = False
    has_symbols = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_numbers = True
        if char in string.punctuation:
            has_numbers = True

    rating1 = len_enough + has_numbers + has_lowercase + has_symbols + has_uppercase
    rating.setText(f'Рейтинг: {'*' * rating1}')

rater.clicked.connect(rate)

window.setLayout(v_line)

app.exec_()
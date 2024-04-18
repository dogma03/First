from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QCheckBox
import string
import random

app = QApplication([])

window = QWidget()
window.resize(300, 300)
window.setWindowTitle('Генератор паролей')
window.show()

v_line = QVBoxLayout()

genB = QPushButton('Сгенерировать пароль.')
gener_pass = QLineEdit()
gener_pass.setReadOnly(True)
len_pass = QLineEdit()
lower_c = QCheckBox('Использовать строчные буквы')
upper_c = QCheckBox('Использовать заглавные буквы')
numbers = QCheckBox('Использовать цифры')
symbols_c = QCheckBox('Использовать символы')
gen_text = QLabel('Сгенерированный пароль:')
len_text = QLabel('Длина сгенерированного пароля:')

v_line.addWidget(gen_text)
v_line.addWidget(gener_pass)
v_line.addWidget(len_text)
v_line.addWidget(len_pass)
v_line.addWidget(lower_c)
v_line.addWidget(upper_c)
v_line.addWidget(numbers)
v_line.addWidget(symbols_c)
v_line.addWidget(genB)

window.setLayout(v_line)

def generate_password():
    try:
        length = int(len_pass.text())
    except:
        gener_pass.setText('Введите длину пароля числом йоу')
        return None

    symbols = ''

    if lower_c.isChecked():
        symbols += string.ascii_lowercase
    if upper_c.isChecked():
        symbols += string.ascii_uppercase
    if numbers.isChecked():
        symbols += string.digits
    if symbols_c.isChecked():
        symbols += string.punctuation
    print(symbols)

    if len(symbols) == 0:
        gener_pass.setText('Выберите хотя бы одну опцию ну пожалуйста чувак')
        return None
    
    password = ''
    for i in range(length):
        password += random.choice(symbols)

    gener_pass.setText(password)

genB.clicked.connect(generate_password)

app.exec_()
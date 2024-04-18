from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QCheckBox

app = QApplication([])

window = QWidget()
window.resize(300, 300)
window.setWindowTitle('Генератор паролей')
window.show()

v_line = QVBoxLayout()

genB = QPushButton('Сгенерировать пароль.')
gener_pass = QLineEdit()
len_pass = QLineEdit()
lower_c = QCheckBox('Использовать строчные буквы.')
upper_c = QCheckBox('Использовать заглавные буквы')
numbers = QCheckBox('Использовать цифры')
symbols = QCheckBox('Использовать символы')
gen_text = QLabel('Сгенерированный пароль:')
len_text = QLabel('Длина сгенерированного пароля:')

v_line.addWidget(gen_text)
v_line.addWidget(gen_text)
v_line.addWidget(gen_text)
v_line.addWidget(gen_text)
v_line.addWidget(gen_text)
v_line.addWidget(gen_text)
v_line.addWidget(gen_text)
v_line.addWidget(gen_text)
v_line.addWidget(gen_text)


window.setLayout(v_line)

app.exec_()
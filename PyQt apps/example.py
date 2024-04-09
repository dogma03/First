from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([]) # выделение места и создание приложения

window = QWidget() # создание окна
window.show() # по умолчанию окно скрыто и нужно его показать

app.exec() # выполнение приложения
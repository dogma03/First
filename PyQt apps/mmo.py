from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QListWidget, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt

# -----------------создание приложения и работа с окном-----------------------
app = QApplication([]) # выделение места и создание приложения

game = QWidget() # создание окна
game.resize(600, 600)
game.setWindowTitle('Игра')
game.show() # по умолчанию окно скрыто и нужно его показать

# ---------------------------визуальная часть приложения-----------------------

# создание направляющих
v_line = QVBoxLayout()
h_line = QHBoxLayout()
low_line = QHBoxLayout()

inventory = QListWidget() # Ну игровая область там текст инвентарь и сё такое
information = QTextEdit()
information.setReadOnly(True)
btn1 = QPushButton('Использовать') # кнопки
btn2 = QPushButton('Защита') #  
btn3 = QPushButton('Удар') #   

h_line.addWidget(inventory) # добалвление всяких панелек
h_line.addWidget(information) #  

v_line.addLayout(h_line)  # закрепление горизонтальной линии на вертикальной направляющей

low_line.addWidget(btn1) # добавление кнопырей
low_line.addWidget(btn2) #  
low_line.addWidget(btn3) #   

v_line.addLayout(low_line) # прикрепление нижней линии к вертикальной

game.setLayout(v_line) # закрепление основного лэйаута для окна

#----------------------------------Классы--------------------------------------------------------

tab = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

class Character():
    def __init__(self, name, hp, armor, power, inventory=[]):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.inventory = inventory
    def print_info(self):
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}')
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}')
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}\nУровень брони: {self.armor}')
        information.setText(f'{tab}Поприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}\nУровень брони: {self.armor}\nСила удара: {self.power}')
    def strike(self, enemy):
        enemy.armor -= self.power
        if enemy.armor <= 0:
            enemy.hp += enemy.armor
            enemy.armor = 0

#---------------------------предметы---------------------------------------------

wooden_sw = inventory.findItems("Деревянный меч", Qt.MatchExactly) #             М    но тут не сами предметы по факту а их нахождение 
br_iron_sw = inventory.findItems("Поломанный железный меч", Qt.MatchExactly) #   Е    в инвентаре
slime_sw = inventory.findItems("Поломанный железный меч", Qt.MatchExactly) #     Ч
legendary_sw = inventory.findItems("Легендарный меч", Qt.MatchExactly) #         И
#--------------------------------------------------------------------------------
leg_armor = inventory.findItems("Легендарная броня старого тёмного лорда", Qt.MatchExactly) # броня имбовая
#--------------------------------------------------------------------------------
slime_core = inventory.findItems("Ядро слайма", Qt.MatchExactly) # ядро обычного слайма(нужно 10 штук для крафта)
king_slime_core = inventory.findItems("Ядро короля слаймов", Qt.MatchExactly) # ядро короля слаймов(для крафта слаймового меча)
chest_key = inventory.findItems("Ключ от сундука", Qt.MatchExactly) # ключ от сундука(для брони)
door_key = inventory.findItems("Ключ от сундука", Qt.MatchExactly) # ключ от ворот в деревню гоблинов(для легендарного меча)
camouflage = inventory.findItems("Гоблинский камуфляж", Qt.MatchExactly) # камуфляж гоблина
#============================персы================================================
knight = Character('Вы', 100, 50, 25) # Главный герой
b_slime = Character('Синий слайм', 25, 5, 5) #  Деф слайм
goblin = Character('Гоблин', 100, 50, 25) #  Гоблен(Габен)

#===================================Функции и всё такое===========================================

def new(): #Вступление
    information.setText(f'{tab}Привет герой, кажись это твой первый раз нахождения в этом мире')
    information.setText(f'{tab}Привет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории')
    information.setText(f'{tab}Привет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории\nПо сюжету ты обычный торговец, но гуляя как-то раз по лесу, ты находишь меч, и решаешь встать на путь путешественника')
    information.setText(f'{tab}Привет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории\nПо сюжету ты обычный торговец, но гуляя как-то раз по лесу, ты находишь меч, и решаешь встать на путь путешественника\nНажми кнопку использовать чтобы начать игру')

#---------------------------первый выбор вначале игры---------------------------------------------

def order_of_fear():
    information.setText(f'''{tab}После того как вы взяли свой меч вы решили вернуться в город из леса в котором вы нашли свой меч, затем когда вы вернулись в город вы увидели такую картину
"Весь город в огне, множество людей орут и бегают по всему городу от страха, верно, на ваш город напали тёмные силы, по словам очевидца в центре города открылся портал и оттуда выбрались эти демоны и нечисть
,они устроили полную разруху, поджигают и взрывают дома, убивают и едят людей, повсюду эти тёмные порталы", увидев это вы в панике зашли в свой дом чтобы собрать вещи и слинять, но под вами открывается портал,
 и по итогу вы падаете из своего дома в потусторонний мир, вы приземлились посреди леса, что будете делать дальше?''')
    btn1.setText('Спрятаться под деревом от страха и рыдать')
    btn2.setText('Убежать из леса и попытаться найти портал')
    btn3.setText('В недоумении искать свою комнату')

#---------------------------итоги первого выбора---------------------------------------------

def new_cry():
    information.setText(f'''{tab}Вас нашёл маленький радиоактивный тёмный паук, вы его не заметили, он вас укусил и вы превратились в полчище таких же пауков, игра окончена.''')
    new()
                       
def new_room(): #             
    information.setText(f'''{tab}Судя по всему вы не заметили того как попали в этот мир и начали искать лестницу чтобы взять важные вещи из спальни на втором этаже.\nИтог: на вас напали тёмные лозы и задушили вас, игра окончена''')
    new()

#-----------------------------плохой выбор--------------------------------------------------------

def new_portal():
    information.setText(f'''{tab}В процессе поиска портала домой вы заметили синего слайма, он выглядел безобидным так как не заметил ВАС, но вы знаете что в этом мире кто угодно готов убить вас, вы решили напасть на него со спины''')
    btn1.setText('Использовать') # кнопки
    btn2.setText('Защита') #   
    btn3.setText('Удар') #    

def print_fight_b_slime(): # сразу и шаблон файта и файт со слаймом
    information.setText(f'''{tab}->УДАР!''')
    knight.strike(b_slime)
    information.setText(f'''{tab}->УДАР!\n{knight.name} атакуете {goblin.name}
используя деревянный меч''')
    information.setText(f'''{tab}->УДАР!\n{knight.name} атакуете {goblin.name}
используя деревянный меч\n{b_slime.name} покачнулся, класс брони: {b_slime.armor}, уровень здоровья: {b_slime.hp}''')
    b_slime.strike(knight)
    information.setText(f'''{tab}->УДАР!\n{knight.name} атакуете {goblin.name}
используя деревянный меч\n{b_slime.name} покачнулся, класс брони: {b_slime.armor}, уровень здоровья: {b_slime.hp}\n
{b_slime.name} атакует вас, используя технику истощения с помощью слаймовой магии''')
    information.setText(f'''{tab}->УДАР!\n{knight.name} атакуете {goblin.name}
используя деревянный меч\n{b_slime.name} покачнулся, уровень брони: {b_slime.armor}, уровень здоровья: {b_slime.hp}\n
{b_slime.name} атакует вас, используя технику истощения с помощью слаймовой магии\n
{knight.name} покачнулись, уровень брони: {knight.armor}, уровень здоровья: {knight.hp}''')

def first_win():
    information.setText(f'{tab}Поздравляем! Вы с невероятной лёгкостью стёрли синего слайма с лица тёмных земель! В награду за вашу победу вы получите ядро слайма')
    inventory.addItem('Ядро слайма')
    information.setText(f'{tab}Поздравляем! Вы с невероятной лёгкостью стёрли синего слайма с лица тёмных земель! В награду за вашу победу вы получите ядро слайма\nЧтобы продолжить нажмите кнопку использовать')

#=========================обнаружение дома из дерева и выбор================================

def find_iron_sw():
    information.setText(f'''{tab}После того как вы уничтожили слайма, вы решили пройтись по тёмному лесу... Спустя час блуждания по тёмным землям вы нашли некое поломанное старое дряхлое здание из тёмного дерева.
    Зайти внутрь?''')

def enter_house():
    information.setText(f'''{tab}По итогу вы решили зайти в дом, внутри дома находится:
     дряхлая кровать, поломанный стол, тумбочка, приоткрытый сундук из которого торчит кончик меча\nЧто осмотрите первым делом?''')

def go_faraway():
    information.setText(f'''{tab}Вы решили пойти дальше и не заходить в дом, пройдя дальше вы ничего не заметили кроме странной пещеры, вы решили вернуться в дом и посмотреть что там''')

def relax():
    information.setText(f'''{tab}После того как вы отдохнули вы решили зайти в этот дом и посмотреть что там(открою секорет, выбора в этих кнопках нет, это иллюзия выбора, психологический трюк, рофел)''')

#-----------------------------выбор внутри дома---------------------------------------------

def check_table(): # осмотр стола
    information.setText(f'''{tab}Получается вы решили первым делом осмотреть стол, вы          
    всего лишь нашли там всякие таблички, бумажки и так далее, на них написано что-то 
    на неизвестном для вас языке. На бумаге написано: ぁ゜゜゜゜👺ぁぁ🥷げごさ しぜぢ\nА
     на табличках написано: げごぢ👺ぁ゜ぁご''')

def check_chest(): # осмотр сундука
    information.setText(f'''{tab}Вы решили посмотреть сундук так как вас заинтересовал 
    меч который торчит оттуда, вы открыли его, и увидели железный меч, вашей радости не 
    было предела, но затем вы заметили что на нём было множество сколов, трещин и так 
    далее, но это всё равно лучше вашей деревянной палки(меча)\nВы решили забрать меч 
    себе и выкинуть старый''')
    inventory.addItem('Железный меч')
    inventory.takeItem('Деревянный меч')

def check_bedside_table(): # осмотр тумбочки
    information.setText(f'''{tab}Вы решили осмотреть тумбочку у дряхлой кровати, открыв 
    её вы обнаружили там ручку из которой потекла паста, опять непонятные бумаги, ну и всё впринципе''')

#==============================запуск всяких функций и так далее============================

new()
if wooden_sw: # Проверка на то есть ли деревянный меч чтобы он не дюпался
    inventory.takeItem('Деревянный меч')
else:
    inventory.addItem('Деревянный меч')

btn1.setText('Использовать') # кнопки
btn2.setText('Защита') #   
btn3.setText('Удар') #    

btn1.clicked.connect(order_of_fear)

btn1.clicked.connect(new_cry)
btn2.clicked.connect(new_portal)
btn3.clicked.connect(new_room)

btn1.clicked.disconnect(new_cry)
btn2.clicked.disconnect(new_portal)
btn3.clicked.disconnect(new_room)

btn1.setText('Использовать') # кнопки
btn2.setText('Защита') #   
btn3.setText('Удар') #    

btn3.clicked.connect(print_fight_b_slime)
btn3.clicked.disconnect(print_fight_b_slime)
btn3.clicked.connect(first_win)

# btn1.setText(f'Войти в дом')
# btn2.setText(f'Пойти дальше')
# btn3.setText(f'Я устал от хождения, лучше посижу')

# btn1.clicked.connect(enter_house)
# btn2.clicked.connect(go_faraway)
# btn3.clicked.connect(relax)

# btn1.disconnect(enter_house)
# btn2.disconnect(go_faraway)
# btn3.disconnect(relax)

# btn1.setText('Осмотреть стол')
# btn2.setText('Осмотреть сундук')
# btn3.setText('Осмотреть тумбочку')

# btn1.clicked.connect(check_table)
# btn2.clicked.connect(check_chest)
# btn3.clicked.connect(check_bedside_table)

# btn1.disconnect(check_table)
# btn2.disconnect(check_chest)
# btn3.disconnect(check_bedside_table)

# btn1.setText('Использовать') # кнопки
# btn2.setText('Защита') #   
# btn3.setText('Удар') #    






app.exec_()
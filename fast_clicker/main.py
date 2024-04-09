import random
import pygame

pygame.init()

TICKRATE = 60

# цвета
BG_COLOR = (154, 205, 50)
CARD_COLOR = (0, 100, 0)
WIN_COLOR = (173, 255, 47)
LOSE_COLOR = (85, 107, 47)

# цвет там, размер окна и т д.
window = pygame.display.set_mode((500, 500)) # размер окна
pygame.display.set_caption('кликер') # название окна
window.fill(BG_COLOR) # цвет фона

clock = pygame.time.Clock()

# отображение карточек
class Card(): 
    def __init__(self, x):
        self.rect = pygame.Rect(x, 170, 70, 100) # Рект именно с большой буквы задает размер и координаты обжекта
        self.color = CARD_COLOR
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render('КЛИК', True, (0, 0, 0))

    def draw(self, need_text):
        pygame.draw.rect(window, self.color, self.rect) # а рект с мелкой просто принтует их
        if need_text:
            window.blit(self.text, (self.rect.x + 5, self.rect.y + 40)) # отображение текста

class Text(): # сам текст
    def __init__(self, x, y, text):
        self.font = pygame.font.Font(None, 30) # выбор шрифта и размера шрифта
        self.text = self.font.render(text, True, (0, 0, 0))  # рендер текста(сам текст, выводить ли, корды)
        self.pos = x, y

    def draw(self): 
        window.blit(self.text, (self.pos))

    def update(self, text): # изменение текста
        self.text = self.font.render(text, True, (0, 0, 0)) # рендер текста(сам текст, выводить ли, корды)

# разделение карточек друг от друга
cards = []
x = 70 
for i in range(4):
    cards.append(Card(x))
    x+= 100

card_cd = 0
timer_cd = TICKRATE # кд таймпера напдписи клик
score = 0
timer = 0


score_text = Text(10, 10, 'Счёт: 0') 
timer_text = Text(10, 40, 'Время: 0')

win_text = Text(160, 220, 'Наконец-то ты победил')
lose_text = Text(180, 220, 'Ура ты проиграл')

state = 'play'

while True: # постоянное отображение окна и т.д. йоу бррр, игровой цикл
    events = pygame.event.get()
    for e in events: # выйти из окна через крестик можно
        if e.type == pygame.QUIT:
            exit()

    if state == 'play':

        if card_cd == 0: # кд надписи клик на карте
            card_cd = TICKRATE // 2
            rand_card = random.randint(0, 3) # где именно появится налпись
            for i in range(4):
                cards[i].color = CARD_COLOR
        else:
            card_cd -= 1
        
        if timer_cd == 0: # сколько времени осталось до результата
            timer += 1
            timer_text.update(f'Время: {timer}')
            timer_cd = TICKRATE
        else:
            timer_cd -= 1

        window.fill(BG_COLOR) # заливка 
        score_text.draw()
        timer_text.draw()

        for i in range(4): # вывод тексат клик на рандомной карте
            if i == rand_card:
                cards[i].draw(True)
            else:
                cards[i].draw(False)

        for e in events: # выйти из окна через крестик можно
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: # если лкм нажата то +1 к очкам
                x, y = e.pos
                for i in range(4):
                    if cards[i].rect.collidepoint(x, y): # проверка столкновения кордов мышки и хитбосков картрчки
                        if i == rand_card:
                            cards[i].color = WIN_COLOR
                            score += 1
                        else:
                            cards[i].color = LOSE_COLOR
                            score -= 1
                        score_text.update(f'Cчёт: {score}')
            if score >= 5 and timer <= 5:
                state = 'win'
            elif score < 5 and timer > 5:
                state = 'lose'

    elif state == 'win':
        window.fill(WIN_COLOR)  
        win_text.draw()

    elif state == 'lose':
        window.fill(LOSE_COLOR)
        lose_text.draw()


    pygame.display.flip() # собственно само постоянное отображение окна
    clock.tick(TICKRATE) # кд таймера
import sys
import pygame
import random

pygame.init()

WIDTH = 336 # разрешение экрана
HEIGHT = 540

window = pygame.display.set_mode((WIDTH, HEIGHT)) 

clock = pygame.time.Clock()

class Background(): # фон
    def __init__(self):
        self.image = pygame.image.load('assets/background.png') # путь
        self.x_1 = 0 # коорды
        self.x_2 = WIDTH


    def draw(self): # вывод
        window.blit(self.image, (self.x_1, 0))
        window.blit(self.image, (self.x_2, 0))

    def update(self): # перемещение и замена картинок чтобы оно показывалось циклично
        self.x_1 -= 1
        self.x_2 -= 1
        if self.x_1 <= -WIDTH:
            self.x_1 = WIDTH
        if self.x_2 <= -WIDTH:
            self.x_2 = WIDTH

class Ground(): # земля
    def __init__(self):
        self.image = pygame.image.load('assets/ground.png') # путь
        self.x_1 = 0 # коорды
        self.x_2 = WIDTH
        self.y = HEIGHT - 100


    def draw(self): # вывож
        window.blit(self.image, (self.x_1, self.y))
        window.blit(self.image, (self.x_2, self.y))

    def update(self): # перемещение и повтореие земли в игре
        self.x_1 -= 2 # скорость перемещ
        self.x_2 -= 2
        if self.x_1 <= -WIDTH: # замена картинки
            self.x_1 = WIDTH
        if self.x_2 <= -WIDTH:
            self.x_2 = WIDTH

class Pipes(): # трубы 
    def __init__(self): 
        self.gate = random.randint(100, HEIGHT - 200)
        self.gap = random.randint(100, 110)

        self.top_image = pygame.image.load('assets/top-pipe.png') # путь к изображению
        self.top_rect = self.top_image.get_rect() # хитбокс
        self.top_rect.bottomleft = (WIDTH, self.gate - self.gap) #  координаты

        self.bot_image = pygame.image.load('assets/bot-pipe.png') # путь к изображению
        self.bot_rect = self.bot_image.get_rect() # хитбокс
        self.bot_rect.topleft = (WIDTH, self.gate + self.gap) # коорды
 
    def draw(self): # вывод трую
        window.blit(self.top_image, self.top_rect)
        window.blit(self.bot_image, self.bot_rect)

    def update(self): # перемещение труб
        self.top_rect.x -= 2
        self.bot_rect.x -= 2
        if self.top_rect.right < 0:
            self.gate = random.randint(100, HEIGHT - 200)
            self.gap = random.randint(32, 45)
            self.top_rect.bottomleft = (WIDTH, self.gate - self.gap) # промежуток между трубами
            self.bot_rect.topleft = (WIDTH, self.gate + self.gap)
            game.score += 1
            game.update_score()

class Bird(pygame.sprite.Sprite): # птипчка
    def __init__(self):
        super().__init__()
        self.image_orig = pygame.image.load('assets/bird.png')
        self.image = self.image_orig
        self.rect = self.image.get_rect(center = (
            WIDTH // 3, # координаты местоположения
            HEIGHT // 2
        ))            
        self.base_speed = -2 #  скорость падения
        self.speed = self.base_speed
        self.angle = 0

    def draw(self):
        window.blit(self.image, self.rect) # рендер птечки
         
    def update(self, events): #  обнова птички
        self.rect.y -= self.speed  #  спид
        if self.speed > self.base_speed:
            self.speed -= 1

        if self.rect.y < 0: 
            self.rect.y = 0
        if self.rect.bottom > HEIGHT - 100:
            self.rect.bottom = HEIGHT - 100

        if self.speed > 0: # угол вращения
            self.angle += 3
            if self.angle > 25:
                self.angle = 25
        if self.speed < 0:
            self.angle -= 1.3
            if self.angle < -40:
                self.angle = -40
        self.image = pygame.transform.rotate(self.image_orig, self.angle)    

        if game.state == 'play': # если стейт это плей то все работает
            for e in events: # 
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        self.speed = 8

            if self.rect.collidelistall([pipes.bot_rect, pipes.top_rect]): #  коллизия с предметами для птечки
                game.state = 'over'
    

class GameManager(): # гейм менеджеп
    def __init__(self):
        self.state = 'play' #  игра типо когда там все двигается
        self.score = 0
        self.font = pygame.font.Font('assets/Flappy-Bird.ttf', 50) # шрифт для счетчика
        self.score_text = self.font.render('0', True, (255, 255, 255))
        self.restart_text = self.font.render('Press R to restart', True, (255, 255, 255))

    def centerx(self, surf):
        return (WIDTH // 2) - (surf.get_width() // 2)

    def centery(self, surf):
        return (HEIGHT // 2) - (surf.get_height() // 2)
    
    def draw_restart(self):
        window.blit(self.restart_text, (self.centerx(self.restart_text), self.centery(self.restart_text)))

    def draw_score(self):
        window.blit(self.score_text, (self.centerx(self.score_text), 10)) # отрисовка счетчика

    def update_score(self):
        self.score_text = self.font.render(str(self.score), True, (255, 255, 255)) # обнова счетчика

    def restart(self):
        self.state = 'play'
        self.score = 0
        self.update_score()


        bird.rect = bird.image.get_rect(center = (
            WIDTH // 3, # координаты местоположения
            HEIGHT // 2
        ))            
        bird.speed = bird.base_speed
        bird.angle = 0

        pipes.gate = random.randint(100, HEIGHT - 200)
        pipes.gap = 60
        pipes.top_rect.bottomleft = (WIDTH,  pipes.gate -   pipes.gap) # промежуток между трубами
        pipes.bot_rect.topleft = (WIDTH, pipes.gate +  pipes.gap)

        

bg = Background() # объекты самой игры типо того
ground = Ground()
pipes = Pipes()
bird = Bird()
game = GameManager()

while True:
    events = pygame.event.get()
    for e in events: # выйти из окна через крестик можно
        if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r and game.state == 'over':
                        game.restart()

        if e.type == pygame.QUIT:
            sys.exit()
    
    if game.state == 'play':
        bg.update() # обновление объектов
        ground.update()
        pipes.update()
    bird.update(events)

    bg.draw() # вывод объектов
    pipes.draw()
    ground.draw()
    bird.draw()
    game.draw_score()
    if game.state == 'over':
        game.draw_restart()

    pygame.display.flip() # собственно само постоянное отображение окна
    clock.tick(60) 
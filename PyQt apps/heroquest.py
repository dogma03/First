class Hero():
    def __init__(self, name, hp, arm_p, power, weapon):
        self.name = name
        self.hp = hp
        self.arm_p = arm_p
        self.power = power
        self.weapon = weapon
    def print_info(self):
        print('Поприветствуйте героя -> ', self.name)
        print('Уровень здоровья:', self.hp)
        print('Класс брони:', self.arm_p)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon, '\n')
    def strike(self, enemy):
        enemy.arm_p -= self.power
        if enemy.arm_p <= 0:
            enemy.hp += enemy.arm_p
            enemy.arm_p = 0

knight = Hero('Ричард', 100, 50, 25, 'Меч')
goblin = Hero('Гоблин', 85, 60, 30, 'Бокопалица')

knight.print_info()
goblin.print_info()

print('Да начнётся битва!')

while knight.hp > 0 or goblin.hp > 0:
    print('-> УДАР!')
    knight.strike(goblin)
    print(knight.name, 'атакует', goblin.name, 'используя', knight.weapon, '\n')
    print(goblin.name, 'покачнулась(-лся)', '\nКласс брони', goblin.name, 'упал до', goblin.arm_p)
    print('Уровень здоровья', goblin.name, 'равен', goblin.hp, '\n')
    print('-> УДАР!')
    goblin.strike(knight)
    print(goblin.name, 'атакует', knight.name, 'используя', goblin.weapon, '\n')
    print(knight.name, 'покачнулась(-лся)', '\nКласс брони', knight.name, 'упал до', knight.arm_p)
    print('Уровень здоровья', knight.name, 'равен', knight.hp, '\n')
if knight.hp <= 0:
    print(knight.name, 'пал в суровом бою.')
if goblin.hp <= 0:
    print(knight.name, 'победил гоблина в суровом бою')
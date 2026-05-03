class Hero:


    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')

    def attack(self):
        print(f'{self.name} наносит удар!')
        self.strength -= 1
        print("сила героя уменьшилась на -1")

    def rest(self):
        print(f'{self.name} отдыхает…')
        self.health += 1
        print("здоровье героя увеличилась на +1")

hero1 = Hero("sj", 10, 100, 10)

hero2 = Hero("ak", 20, 200, 20)


hero1.greet()
hero1.attack()
hero1.rest()
hero2.greet()
hero2.attack()
hero2.rest()
#test
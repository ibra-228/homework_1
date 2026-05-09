import random


class Hero:
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.lvl}')

    def attack(self):
        print(f'{self.name} наносит удар!')

    def rest(self):
        print(f'{self.name} отдыхает…')
        self.health += 1
        print("здоровье героя увеличилась на +1")

class Warrior(Hero):
    def __init__(self, name, lvl, health, strength, stamina):
        super().__init__(name, lvl, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f'Воин {self.name} атакует мечом!')

class Mage(Hero):
    def __init__(self, name, lvl, health, strength, mp):
        super().__init__(name, lvl, health, strength)
        self.mp = mp

    def attack(self):
        print(f'Маг {self.name} кастует заклинание!')

class Assassin(Hero):
    def __init__(self, name, lvl, health, strength, stealth):
        super().__init__(name, lvl, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f'Ассасин {self.name} атакует из-под тишка!')


Warrior1 = Warrior("Kit", 10, 100, 20, 100)
Mage1 = Mage("Spike", 11, 110, 10, 100)
Assassin1 = Assassin("Colt", 10, 90, 15, 100)

def play_minigame():
    player = input("Выберите героя (Warrior / Mage / Assassin): ").lower()
    choices = ["warrior", "mage", "assassin"]
    enemy = random.choice(choices)
    print(f"Вы выбрали: {player}")
    print(f'Противник: {enemy}')

    if player == enemy:
        print("Ничья!")

    elif (player == "warrior" and enemy == "assassin") or (player == "assassin" and enemy == "mage") or (player == "mage" and enemy == "warrior"):
        print("Победа!")

    else:
        print("Проиграл!")


play_minigame()



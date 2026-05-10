from abc import abstractmethod, ABC

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')

    def rest(self):
        print(f'{self.name} отдыхает')
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        print(f'Воин {self.name} атакует мечом')

class Mage(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        print(f'Маг {self.name} использует магию')

class Assassin(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        print(f'Ассасин {self.name} атакует из-под тишка')

warrior1 = Warrior("Smith", 10, 200, 20)
mage1 = Mage("magik", 10, 100, 10)
assassin1 = Assassin("kit", 10, 150, 15)

warrior1.greet()
warrior1.attack()
warrior1.rest()

mage1.greet()
mage1.attack()
mage1.rest()

assassin1.greet()
assassin1.attack()
assassin1.rest()


from entity import Entity
from random import randint

class Dragon(Entity):
    '''
    Class representing a dragon character, inheriting from Entity.

    Methods:
        basic_attack(self, other): Represents a basic attack action.
        special_attack(self, other): Represents a special attack action.
    '''
    def basic_attack(self, other):
        damage = randint(3, 7)
        other.take_damage(damage)
        return f'{self.name} smashes you with its tail for {damage} damage!'
    
    def special_attack(self, other):
        damage = randint(4, 8)
        other.take_damage(damage)
        return f'{self.name} slashes you with its claws for {damage} damage!'
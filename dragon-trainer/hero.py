from entity import Entity
from random import randint

class Hero(Entity):
    '''
    Class representing a hero character, inheriting from Entity.

    Methods:
        basic_attack(self, other): Represents a basic attack action.
        special_attack(self, other): Represents a special attack action.
    '''
    def basic_attack(self, other):
        damage = randint(1,6) + randint(1,6)
        other.take_damage(damage)
        return f'{self.name} slashes the {other.name} with their sword for {damage} damage!'
    
    def special_attack(self, other):
        damage = randint(1,12)
        other.take_damage(damage)
        return f'{self.name} hits the {other.name} with an arrow for {damage} damage!'
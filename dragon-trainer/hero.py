from entity import Entity
from random import randint

class Hero(Entity):
    def basic_attack(self, other):
        damage = randint(1,6) + randint(1,6)
        other.take_damage(damage)
        return f'{self.name} slashes the {other.name} with their sword for {damage} damage!'
    
    def special_attack(self, other):
        damage = randint(1,12)
        other.take_damage(damage)
        return f'{self.name} hits the {other.name} with an arrow for {damage} damage!'
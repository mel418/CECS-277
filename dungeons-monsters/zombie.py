from entity import Entity
from random import randint

class Zombie(Entity):
    def __init__(self):
        name = 'Rotten Zombie'
        max_hp = randint(8, 10)
        super().__init__(name, max_hp)

    def attack(self, entity):
        dmg = randint(5, 12)
        entity.take_damage(dmg)  # Use take_damage method to handle damage
        return self.name + ' attacks a ' + entity.name + ' for ' + str(dmg) + ' damage.'
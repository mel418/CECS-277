from entity import Entity
from random import randint

class Skeleton(Entity):
    def __init__(self):
        name = 'Spooky Skeleton'
        max_hp = randint(6, 10)
        super().__init__(name, max_hp)

    def attack(self, entity):
        dmg = randint(6, 10)
        entity.take_damage(dmg)  # Use take_damage method to handle damage
        return self.name + ' attacks a ' + entity.name + ' for ' + str(dmg) + ' damage.'
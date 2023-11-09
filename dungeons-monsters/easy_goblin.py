from random import randint
from entity import Entity


class EasyGoblin(Entity):
    def __init__(self):
        hp = randint(4, 6)
        super().__init__('Lurking Goblin', hp)

    def attack(self, entity):
        damage = randint(2, 5)
        entity.take_damage(damage)  # Use take_damage method to handle damage
        return self.name + ' attacks a ' + entity.name + ' for ' + str(damage) + ' damage.'

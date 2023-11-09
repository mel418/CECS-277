from random import randint
from entity import Entity


class EasyZombie(Entity):
    def __init__(self):
        hp = randint(4, 5)
        super().__init__('Jumping Zombie', hp)

    def attack(self, entity):
        damage = randint(1, 5)
        entity.take_damage(damage)  # Use take_damage method to handle damage
        return self.name + ' attacks a ' + entity.name + ' for ' + str(damage) + ' damage.'

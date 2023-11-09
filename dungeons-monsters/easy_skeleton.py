from random import randint
from entity import Entity


class EasySkeleton(Entity):
    def __init__(self):
        hp = randint(3, 4)
        super().__init__('Vengeful Skeleton', hp)

    def attack(self, entity):
        damage = randint(1, 4)
        entity.take_damage(damage)  # Use take_damage method to handle damage
        return self.name + ' attacks a ' + entity.name + ' for ' + str(damage) + ' damage.'

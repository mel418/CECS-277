from entity import Entity
from random import choice, randint

class Enemy(Entity):
    def __init__(self):
        name = choice(['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie'])
        hp = randint(4, 8)
        super().__init__(name, hp)

    def attack(self, entity):
        damage = randint(1, 4)
        entity.take_damage(damage)  # Use take_damage method to handle damage
        return self.name + ' attacks a ' + entity.name + ' for ' + str(damage) + ' damage.'

# monster = Enemy()
# print(monster.name)

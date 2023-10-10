from dragon import Dragon
from random import randint

class FlyingDragon(Dragon):
    def __init__(self, name, max_hp, swoops) -> None:
        super().__init__(name, max_hp)
        self.swoops = swoops

    def special_attack(self, other):
        if self.swoops > 0:
            self.swoops -= 1
            damage = randint(5, 8)
            other.take_damage(damage)
            return f'{self.name} swoops at you for {damage} damage!'
        else:
            return f'{self.name} tries to swoop down to hit you, but failed.'
        
    def __str__(self) -> str:
        entity_info = super().__str__()
        return f"{entity_info} \nSwoop attacks remaining: {self.swoops}"
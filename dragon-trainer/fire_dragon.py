from dragon import Dragon
from random import randint

class FireDragon(Dragon):
    def __init__(self, name, max_hp, f_shots) -> None:
        super().__init__(name, max_hp)
        self.fire_shots = f_shots
    
    def special_attack(self, other):
        if self.fire_shots > 0:
            self.fire_shots -= 1
            damage = randint(5, 9)
            other.take_damage(damage)
            return f'{self.name} engulfs you in flames for {damage} damage!'
        else:
            return f'{self.name} tries to spit fire at you but is all out of fire shots.'
        
    
    def __str__(self) -> str:
        entity_info = super().__str__()
        return f"{entity_info} \nFire Shots remaining: {self.fire_shots}"
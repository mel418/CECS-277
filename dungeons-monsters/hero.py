import random
from entity import Entity


class Hero(Entity):
    def __init__(self, name):
        self._loc = [0, 0]
        super().__init__(name, 25)

    def attack(self, entity):
        dmg = random.randint(2, 5)
        entity.take_damage(dmg)
        return f"{self.name} attacks a {entity.name} for {dmg} damage."

    def go_north(self):
        if 0 <= self._loc[0] - 1 <= len(m)-1:
            self._loc[0] = self._loc[0] - 1
            return m[self._loc[0]][self._loc[1]]
        else:
            return 'o'

    def go_south(self):
        if 0 <= self._loc[0] + 1 <= len(m)-1:
            self._loc[0] = self._loc[0] + 1
            return m[self._loc[0]][self._loc[1]]
        else:
            return 'o'

    def go_east(self):
        if 0 <= self._loc[1] + 1 <= len(m[r])-1:
            self._loc[1] = self._loc[0] + 1
            return m[self._loc[0]][self._loc[1]]
        else:
            return 'o'

    def go_west(self):
        if 0 <= self._loc[1] - 1 <= len(m[r])-1:
            self._loc[1] = self._loc[0] - 1
            return m[self._loc[0]][self._loc[1]]
        else:
            return 'o'
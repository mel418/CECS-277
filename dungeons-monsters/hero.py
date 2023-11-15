from random import randint
from entity import Entity
from map import Map  # Import the Map class

class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, 25)
        self._loc = [0, 0]
        

    @property
    def get_loc(self):
        return self._loc

    def attack(self, entity):
        dmg = randint(2, 5)
        entity.take_damage(dmg)
        return f"{self.name} attacks a {entity.name} for {dmg} damage."

    def go_north(self):
        if self.get_loc[0] > 0:
            self._loc[0] -= 1
            return Map()[self.get_loc[0]][self.get_loc[1]]
        else:
            return 'o'

    def go_south(self):
        if self.get_loc[0] < len(Map()[self.get_loc[0]]) - 1:
            self._loc[0] += 1
            return Map()[self.get_loc[0]][self.get_loc[1]]
        else:
            return 'o'

    def go_east(self):
        if self.get_loc[1] < len(Map()[self.get_loc[1]]) - 1:
            self.get_loc[1] += 1
            return Map()[self.get_loc[0]][self.get_loc[1]]
        else:
            return 'o'

    def go_west(self):
        if self.get_loc[1] > 0:
            self.get_loc[1] -= 1
            return Map()[self.get_loc[0]][self.get_loc[1]]
        else:
            return 'o'


# # Example usage
# map_singleton = Map()  # You should have the Map class implemented and map loaded
# hero = Hero("YourHeroName")
# print(map_singleton.show_map(hero._loc))
# print(hero.go_north())  # Move north and check the location
# print(hero.go_east())  # Move north and check the location


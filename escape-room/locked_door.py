from door import Door
from random import randint

class LockedDoor(Door):
    def __init__(self) -> None:
        self._key_location = randint(1,3)
        self._input = None

    def examine_door(self):
        return 'You encounter a locked door. Look around for the key.'
    
    def menu_options(self):
        return '1. Look under the mat \n2. Look under the flower pot \n3. Look under the fake rock.\n'
    
    def get_menu_max(self):
        return 3
    
    def attempt(self, option):
        self._input = option

    
    def is_unlocked(self):
        return self._input == self._key_location
    
    def clue(self):
        return 'Look somewhere else'
        
    
    def success(self):
        # self._input = None
        # self._correct_value = randint(1,10)
        return 'You found the key and unlocked the door.\n'

    

from door import Door
from random import choice

class CodeDoor(Door):
    def __init__(self) -> None:
        self._correct_code = [choice(['X', 'O']) for _ in range(3)]
        self._input = [choice(['X', 'O']) for _ in range(3)]

    def examine_door(self):
        return 'You encounter A door with a coded keypad with three characters. \nEach key toggles a value with an ‘X’ or an ‘O’.'
    
    def menu_options(self):
        return f'{" ".join(self._input)} \n1. Press Key 1 \n2. Press Key 2 \n3. Press Key 3\n'
    
    def get_menu_max(self):
        return 3
    
    def attempt(self, option):
        self._input[option-1] = 'X' if self._input[option-1] == 'O' else 'O'
        return f'You pressed Key {option}. The code is now: {" ".join(self._input)}'
    
    def is_unlocked(self):
        return self._input == self._correct_code
    
    def clue(self):
        correct_characters = sum(1 for i in range(3) if self._input[i] == self._correct_code[i])
        return f'The number of correct characters: {correct_characters}'
        
    
    def success(self):
        # self._input = None
        # self._correct_value = randint(1,10)
        return f'You found the correct code and opened the door. Correct Code: {" ".join(self._input)}\n'

    

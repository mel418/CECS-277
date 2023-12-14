from puppy import Puppy
from check_input import get_int_range

def main():
    pup = Puppy()
    print('Congratulations on your new puppy!')
    while True:
        # print(pup._state)
        choice = get_int_range(
            'What would you like to do?'
            '\n1. Feed the puppy'
            '\n2. Play with the puppy'
            '\n3. Quit'
            '\nEnter choice: ',1,3)
        
        if choice == 1:
            print(pup.give_food())
        
        elif choice == 2:
            print(pup.throw_ball())

        elif choice == 3:
            break

main()
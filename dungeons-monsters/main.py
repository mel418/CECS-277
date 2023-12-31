from map import Map
from hero import Hero
from beginner_factory import BeginnerFactory
from expert_factory import ExpertFactory

from check_input import get_int_range
from random import choice

def main():
    name = input('What is your name, traveler? ')
    difficulty = get_int_range('Difficulty:\n'
                                '1.Beginner\n'
                                '2.Expert\n', 1, 2)
    dungeon = Map()
    hero = Hero(name)
    if difficulty == 1:
        difficulty = BeginnerFactory()
    elif difficulty == 2:
        difficulty = ExpertFactory()
    counter = 0
    while hero.hp > 0:
        dungeon.reveal(hero.get_loc)
        print(hero, hero.get_loc)
        print(dungeon.show_map(hero.get_loc))
        move = get_int_range(
                            '1. Go North\n'
                            '2. Go South\n'
                            '3. Go East\n'
                            '4. Go West\n'
                            '5. Quit\n'
                            'Enter choice: '
                            , 1, 5
                            )
        if move == 1:
                encounter = hero.go_north()
        elif move == 2:
            encounter = hero.go_south()
        elif move == 3:
            encounter = hero.go_east()
        elif move == 4:
            encounter = hero.go_west()
        elif move == 5:
            break
        
        print(f'Tile: {encounter}')
        if encounter == 'm':
             monster = difficulty.create_random_enemy()
             print(f'You encounter a {monster}')
             dungeon.reveal(hero.get_loc)
             while monster.hp > 0 and hero.hp > 0:
                turn = get_int_range(f'1. Attack {monster.name}\n'
                                       '2. Run Away\n'
                                       'Enter choice: ', 1, 2)
                if turn == 1:
                    print(hero.attack(monster))
                    if monster.hp > 0:
                        print(monster.attack(hero))
                    else:
                        print(f'You have slain a {monster.name}!')
                        dungeon.remove_at_loc(hero.get_loc)
                elif turn == 2:
                    print('You ran away!')
                    while choice([hero.go_north, hero.go_south, hero.go_east, hero.go_west])() == 'o':
                        continue

                    break                
                  
        elif encounter == 'o':
             print('You cannot go that way...')

        elif encounter == 'n':
            print('There is nothing here...')
        
        elif encounter == 's':
            print(f'{hero.name} has wounded up back at the start of the dungeon...')

        elif encounter == 'i':
            if hero.hp < 25:
                print('You found a Health Potion! You drink it to restore your health.')
                hero.heal()
                dungeon.remove_at_loc(hero.get_loc)
            else:
                print(f'You found a Health Potion! \nBut your health is still full so you decide to put back the health potion.')

        elif encounter == 'f':
            print('\nCongratulations! You found the stairs to the next floor of the dungeon.')
            counter += 1
            if counter == 3:
                counter = 0
            print(f'Counter: {counter+1}')
            dungeon.load_map(counter+1)

        print()

        if hero.hp <= 0:
            print(f'\nHero {hero.name} is dead...')
            break
    print('Game Over')    

main()
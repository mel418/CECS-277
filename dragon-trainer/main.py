from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from check_input import get_int_range
from random import choice

def main():
    name = str(input('What is your name, challenger?\n'))
    hero = Hero(name, 50)
    dragons = [
        Dragon('Deadly Nadder', 10),
        FireDragon('Gronckle', 15, 3),
        FlyingDragon('Timberjack', 20, 5),
        FireDragon('Bartholomew', 200, 1),
    ]
    total_dragons = len(dragons)
    print(f'Welcome to dragon training, {name} \nYou must defeat {total_dragons} dragons.')
    while len(dragons) > 0 and hero.hp > 0:
        print(f'\n{hero} \nLevel: {hero.level}')
        [print(f"{i+1}. Attack {dragon}") for i, dragon in enumerate(dragons)]
        dragonChoice = get_int_range(f'Choose a dragon to attack: ', 1, len(dragons)) - 1
        weaponChoice = get_int_range('\nAttack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)\nEnter weapon: ', 1, 2)
        if weaponChoice == 1:
            print()
            print(hero.basic_attack(dragons[dragonChoice]))
        else:
            print()
            print(hero.special_attack(dragons[dragonChoice]))

        if dragons[dragonChoice].hp <= 0:
            print(f'{hero.name} has slain {dragons[dragonChoice].name}\n')
            dragons.pop(dragonChoice)
            hero.level += 1

        if not dragons: print(f'Congratulations! You have defeated all {total_dragons} dragons, you have passed the trials.'); break

        random_dragon = choice([dragon for dragon in dragons])
        attack_type = choice(["basic", "special"])

        # Determine which attack method to call based on the attack_type
        if attack_type == "basic":
            print(random_dragon.basic_attack(hero))
        else:
            print(random_dragon.special_attack(hero))

        if hero.hp <= 0:
            print(f'{hero.name} is knocked out')
            break
    

main()
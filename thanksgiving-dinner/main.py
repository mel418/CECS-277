from check_input import get_int_range
from large_plate import LargePlate
from small_plate import SmallPlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie

def examine_plate(p):
    print(p.description())
    if p.weight() <= 0 or p.area() <= 0:
        if p.area() <= 0:
            print(
                'Your plate isn\'t big enough for this much food! Your food spills over the edge.')
        else:
            print(
                'Your plate isn\'t strong enough to carry this much food! Your food spills over the edge.')
        return True
    
    if p.weight() >= 13:
        print('Sturdiness: Strong')
    elif p.weight() <= 12 and p.weight() >= 7:
        print('Sturdiness: Weak')
    elif p.weight() <= 6:
        print('Sturdiness: Bending')
    
    if p.area() >= 41:
        print('Space available: Plenty')
    elif p.area() <= 40 and p.area() >= 21:
        print('Space available: Some')
    elif p.area() <= 20:
        print('Space available: a tiny bit')
    
    return False
    
def main():
    print(
        '- Thanksgiving Dinner -\n'
        'Serve yourself as much food as you like from the buffet, but make sure\n'
        'that your plate will hold without spilling everywhere!')
    
    plate_choice = get_int_range(
                        'Choose a plate:\n'
                        '1. Small Sturdy Plate\n'
                        '2. Large Flimsy Plate\n', 1, 2)
    
    if plate_choice == 1:
        p = SmallPlate()
    elif plate_choice == 2:
        p = LargePlate()

    while p.area() > 0 and p.weight() > 0:
        food_choice = get_int_range(  
                                    '1. Turkey\n'
                                    '2. Stuffing\n'
                                    '3. Potatoes\n'
                                    '4. Green Beans\n'
                                    '5. Pie\n'
                                    '6. Quit\n',1, 6,)
        if food_choice == 1:
            p = Turkey(p)
        elif food_choice == 2:
            p = Stuffing(p)
        elif food_choice == 3:
            p = Potatoes(p)
        elif food_choice == 4:
            p = GreenBeans(p)
        elif food_choice == 5:
            p = Pie(p)
        elif food_choice == 6:
            print(p.description())
            print(
                f'Good job! You made it to the table with {p.count()} items.\n'
                f'There was still {p.area()} square inches left on your plate.\n'
                f'Your plate could have held {p.weight()} more ounces of food.\n'
                'Don\'t worry, you can always go back for more. Happy Thanksgiving!')
            break

        if examine_plate(p):
            break

        # print(f'Area: {p.area()}\nWeight: {p.weight()}')
    


main()
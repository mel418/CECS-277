import random
import check_input

def main():
  print('==== Ship, Captain, and Crew! ====\n')
  playerpoints = [0,0] 
  count = 0
  for i in range(2):
    die_keep = []
    die_roll = [0,0,0,0,0]
    print(f"Player #{i+1}'s Turn: ")
    while count<3:
      roll_dice(die_roll)
      display_dice('Roll ', die_roll)
      if 4 not in die_keep:
        if 6 in die_roll and 6 not in die_keep:
          print("Yo ho ho! Ye secured a ship!")
          die_keep.append(6) 
          die_roll.remove(6)
          if 5 in die_roll:
            print("Shiver me timbers! A Capt'n!")
            die_keep.append(5)
            die_roll.remove(5)
            if 4 in die_roll:
              print("Ye bribed a crew with Grog!")
              die_keep.append(4)
              die_roll.remove(4)
        if 6 in die_keep and 5 not in die_keep and 5 in die_roll:
          print("Shiver me timbers! A Capt'n!")
          die_keep.append(5)
          die_roll.remove(5)
          if 4 in die_roll:
            print("Ye bribed a crew with Grog!")
            die_keep.append(4)
            die_roll.remove(4)
        if 5 in die_keep and 4 not in die_keep and 4 in die_roll:
          print("Ye bribed a crew with Grog!")
          die_keep.append(4)
          die_roll.remove(4)
      
      display_dice('Keep', die_keep)
      if [6,5,4] == die_keep:
        display_dice('Cargo',die_roll)
        playerpoints[i] = die_roll[0] + die_roll[1]
        print(f"")


      if count != 2:
        choice = check_input.get_yes_no('\nRoll again? ')
      else:
        break

      if not choice:
        break
      elif choice:
        count +=1

    print(f"Player# {i+1} points = {playerpoints[i]}")
    
    i +=1
    count =0
    
  
  
  findwinner(playerpoints)

def roll_dice(dice):
  for i in range(len(dice)):
    dice[i] = random.randint(1,6)
  dice.sort(reverse = True)
  return dice

def display_dice(name,dice):
    print(f"{name} = {' '.join([str(i) for i in dice])}")
    print()
  

def findwinner(playerpoints):
    print("\nScore: ")
    print(f"Player #1 = {playerpoints[0]}")
    print(f"Player #2 = {playerpoints[1]}")
    if playerpoints[0] > playerpoints[1]:
        print("Player #1 won!")
    elif playerpoints[1] > playerpoints[0]:
      print("Player #2 won!")
    else:
        print("It was a tie!")


main()
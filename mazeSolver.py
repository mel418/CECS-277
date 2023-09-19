# Melody Gatan, Kenton La
# 9/12/2023
# desc
import check_input

def main():
    print("-Maze Solver-")
    maze_array = read_maze()
    loc = find_start(maze_array)
    print(loc)
    

    while maze_array[loc[0]][loc[1]] != 'f':
        display_maze(maze_array, loc)
        print(
        "\n1. Go North"
        "\n2. Go South"
        "\n3. Go East"
        "\n4. Go West"
        )
        

        choice = check_input.get_int_range("Enter choice: ", 1, 4)

        if choice == 1:
            new_loc = [loc[0] - 1, loc[1]]
        elif choice == 2:
            new_loc = [loc[0] + 1, loc[1]]
        elif choice == 3:
            new_loc = [loc[0], loc[1] + 1]
        elif choice == 4:
            new_loc = [loc[0], loc[1] - 1]

        if maze_array[new_loc[0]][new_loc[1]] == '*':
            print("You cannot move there.")
        else:
            loc = new_loc
        
    display_maze(maze_array, loc) 
    print("Congratulations! You solved the maze.")


def read_maze():
    maze_array = []
    maze = open('maze.txt', 'r')
    for line in maze:
        inner_list = []
        for char in line:
            if char != '\n':
                inner_list.append(char)
        maze_array.append(inner_list)
    return maze_array


def find_start(maze):
    r = 0
    for row in maze:
        c = 0
        for col in row:
            if col == 's':
                return [r, c]
            c += 1
        r += 1


def display_maze(maze, loc):
    r = 0
    for row in maze:
        c = 0
        for col in row:
            if [r, c] == loc:
                print('X', end='')
            else:
                print(col, end='')
            c += 1
        print()
        r += 1

main()
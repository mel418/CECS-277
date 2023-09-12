# Melody Gatan, Kenton La
# 9/12/2023
# desc
#import check_input

def main():
    print("-Maze Solver-")
    maze_array = read_maze()

    loc = find_start(maze_array)
    # print(loc)
    display_maze(maze_array, loc)

    print(
    "\n1. Go North"
    "\n2. Go South"
    "\n3. Go East"
    "\n4. Go West"
    )

    userInput = input


def read_maze():
    with open("maze.txt", "r") as maze:
        return maze.readlines()

def find_start(maze):
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == 's':
                return [r+1, c+1]

def display_maze(maze, loc):
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if [r+1, c+1] == loc:
                print('X', end='')
            else:
                print(col, end='')

main()
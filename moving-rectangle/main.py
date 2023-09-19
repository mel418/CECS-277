# Melody Gatan, Kenton La
# 9/19/2023
# Creates a 20x20 grid and lets the user create a rectangle that they can move around on the grid
import rectangle
import check_input


def display_grid(grid):
    r = 0
    for row in grid:
        c = 0
        for col in row:
            print(col, end=' ')
        c += 1
        print()
    r += 1


def reset_grid(grid):
    for i in range(20):
        col = []
        for j in range(20):
            col.append('.')
        grid.append(col)
        i += 1

def place_rect(grid, rect):
    print(rect.get_coords(), rect.get_dimensions())
    x =  rect.get_coords()[0]
    y = rect.get_coords()[1]
    height = rect.get_dimensions()[1]
    width = rect.get_dimensions()[0]
    r = 0
    coord_found = False
    for row in grid:
        c = 0
        for col in row:
            if r == y and c == x:
                coord_found = True
                grid[r][c] = "*"
            elif coord_found:
                for r in range(height):
                    for c in range(width):
                        grid[r+y][c + x] = "*"
            c += 1
        r += 1

    display_grid(grid)



def main():
    grid = []
    choice = 0
    reset_grid(grid)
    w = check_input.get_int_range("Enter rectangle width (1-5): ", 1, 5)
    h = check_input.get_int_range("Enter rectangle height (1-5): ", 1, 5)
    rect = rectangle.Rectangle(w, h)
    place_rect(grid, rect)

    
    while choice != 5:
        print("\nEnter Direction:")
        print("1. Up\n2. Down\n3. Left\n4. Right\n5. Quit")

        choice = check_input.get_int_range("Select an option (1-5): ", 1, 5)

        if choice == 1:
            rect.move_up()
        elif choice == 2:
            rect.move_down()
        elif choice == 3:
            rect.move_left()
        elif choice == 4:
            rect.move_right()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please select a valid option.")

        # Clear the previous position of the rectangle
        grid = []
        reset_grid(grid)
        # Place the rectangle in its new position
        place_rect(grid, rect)

main()


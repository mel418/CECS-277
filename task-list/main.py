from check_input import get_int_range
from tasklist import Tasklist

def main_menu():
    print(
        "1. Display current task"
        "\n2. Display all tasks"
        "\n3. Mark current task complete"
        "\n4. Add new task"
        "\n5. Search by date"
        "\n6. Save and quit"
    )
    choice = get_int_range("Enter choice: ", 1, 6)
    return choice


def get_date():
    month = get_int_range("Enter month: ", 1, 12)
    day = get_int_range("Enter day: ", 1, 31)
    year = get_int_range("Enter year: ", 2000, 3000)
    return f"{month:02d}/{day:02d}/{year}"


def get_time():
    print("Enter time:")
    hour = get_int_range("Enter hour: ", 0, 23)
    minute = get_int_range("Enter minute: ", 0, 59)
    return f"{hour:02d}:{minute:02d}"


def main():
    choice = 0
    tl = Tasklist()
    while choice != 6:
        length = len(tl)
        print("-Tasklist-")
        print(f"Tasks to complete: {length}")
        choice = main_menu()
        if choice == 1:
            if length == 0:
                print("All tasks are completed.")
                print()
            else:
                print('Current task is:')
                print(tl.get_current_task())
                print()

        elif choice == 2:
            if length == 0:
                print("All tasks are completed.")
                print()
            else:
                print('Tasks:')
                i = 1
                for task in tl:
                    print(f'{i}. {task}')
                    i+=1
                print()

        elif choice == 3:
            if length == 0:
                print("All tasks are completed.")
                print()
            else:
                print('Marking current task as complete:')
                print(tl.get_current_task())
                tl.mark_complete()
                print('New current task is:')
                print(tl.get_current_task())
                print()

        elif choice == 4:
            description = input('Enter a task: ')
            print("Enter due date:")
            date = get_date()
            time = get_time()
            tl.add_task(description, date, time)
            print()

        elif choice == 5:
            print('Enter date to search: ')
            user_date = get_date()
            print(f'Tasks due on {user_date}\n')
            i = 1
            for task in tl:
                if task.date == user_date:
                    print(f'{i}. {task}')
                i+=1

        elif choice == 6:
            tl.save_file()

main()
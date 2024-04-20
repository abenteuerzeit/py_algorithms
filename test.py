import os
import random

from linear_search import linear_search
from binary_search import binary_search


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid integer.")


def get_custom_range():
    start = get_int_input("Enter the start of the range: ")
    end = get_int_input("Enter the end of the range (inclusive): ")
    if start <= end:
        return list(range(start, end + 1))
    else:
        print("Start must be less than or equal to end.")
        return get_custom_range()


def get_random_list():
    size = get_int_input("Enter the size of the list: ")
    if size <= 0:
        print("Size must be positive.")
        return get_random_list()
    max_value = get_int_input("Enter the maximum value in the list: ")
    if max_value < size - 1:
        print("Maximum value must be at least size - 1 to ensure uniqueness.")
        return get_random_list()
    numbers = random.sample(range(max_value + 1), size)
    numbers.sort()
    return numbers


def update_number_list():
    print("1. Define a custom range for the list")
    print("2. Generate a random list")
    choice = input("Select an option (1-2): ")
    if choice == '1':
        return get_custom_range()
    elif choice == '2':
        return get_random_list()
    else:
        print("Invalid choice.")
        return update_number_list()


def search(numbers, function):
    if numbers is None:
        print("Number list is not set. Please set it under Settings.")
        return
    target = get_int_input("Enter target number: ")
    result = function(numbers, target)
    verify(result)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    numbers = [n for n in range(10)]  # Initial list
    actions = {'1': linear_search, '2': binary_search}

    while True:
        clear_screen()
        print("""
Number List Options
---
1. Linear search
2. Binary search
3. Settings
4. Quit
---
Current List: {0}
""".format(numbers))
        option = input("Select (1-4): ")

        if option in actions:
            search(numbers, actions[option])
        elif option == '3':
            numbers = update_number_list() or numbers
            if numbers:
                numbers.sort()
                print("New number list:", numbers)
            else:
                print("Error setting new number list.")
        elif option == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

        if input("Continue? (y/n): ").lower() != 'y':
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()


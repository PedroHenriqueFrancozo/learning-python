"""
Topic: Exercise - Shopping List
Focus: Implementing a CLI (Command Line Interface) for list management.
"""
import os

shopping_list = []

while True:
    print("\nSelect an option")
    option = input("[i]nsert [d]elete [l]ist [e]xit: ").lower()
    
    if option == "i":
        os.system('clear') # or 'cls' for Windows
        value = input("Item name: ")
        shopping_list.append(value)
        print(f'"{value}" added successfully!')

    elif option == "d":
        os.system('clear')
        try:
            # Using index to delete is usually safer in this exercise
            index_str = input("Choose the index to delete: ")
            index = int(index_str)
            removed_item = shopping_list.pop(index)
            print(f'Item "{removed_item}" removed successfully!')
        except ValueError:
            print("Please enter a valid integer number.")
        except IndexError:
            print("This index does not exist in the list.")
        except Exception:
            print("Unknown error occurred.")

    elif option == "l":
        os.system('clear')
        if not shopping_list:
            print("The list is empty.")
        
        for i, item in enumerate(shopping_list):
            print(f'{i} - {item}')

    elif option == "e":
        break
    
    else:
        print("Invalid option. Please choose i, d, or l.")
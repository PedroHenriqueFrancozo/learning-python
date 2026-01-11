"""
Exercise: Find the first duplicate integer
Requirements:
    The duplicate is defined by the second occurrence of a number.
    Example: [1, 2, 3, 3, 2, 1] -> returns 3.
    If no duplicates are found, return -1.
"""

integer_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def find_first_duplicate(integers):
    checked_numbers = set()
    first_duplicate = -1

    for number in integers:
        if number in checked_numbers:
            first_duplicate = number
            break

        checked_numbers.add(number)

    return first_duplicate


for sub_list in integer_lists:
    result = find_first_duplicate(sub_list)
    print(f"{sub_list} | Result: {result}")
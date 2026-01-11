"""
Lesson 81: Introduction to Lambda Functions (Anonymous Functions)
Lambda functions are one-line functions that consist of a single expression.
"""

people_list = [
    {'name': 'Luiz', 'last_name': 'Miranda'},
    {'name': 'Maria', 'last_name': 'Oliveira'},
    {'name': 'Daniel', 'last_name': 'Silva'},
    {'name': 'Eduardo', 'last_name': 'Moreira'},
    {'name': 'Aline', 'last_name': 'Souza'},
]

def display_list(target_list):
    for item in target_list:
        print(item)
    print()

# Using lambda to sort by name
# item represents each dictionary in the list
sorted_by_name = sorted(people_list, key=lambda item: item['name'])

# Using lambda to sort by last name
sorted_by_last_name = sorted(people_list, key=lambda item: item['last_name'])

print("Sorted by Name:")
display_list(sorted_by_name)

print("Sorted by Last Name:")
display_list(sorted_by_last_name)
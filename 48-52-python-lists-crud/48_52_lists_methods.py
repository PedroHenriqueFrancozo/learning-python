"""
Topic: Python Lists (Type list)
Focus: Mutability, CRUD operations, memory management, and methods.
"""

# 1. Basics & Mutability
# Lists can hold any data type and are mutable (can be changed in place).
lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'  # Updating value at index -3
print(f"Updated list: {lista}")

# 2. CRUD (Create, Read, Update, Delete)
lista_numerica = [10, 20, 30, 40]
lista_numerica.append(50)          # ADD to the end
removed_value = lista_numerica.pop(3) # REMOVE by index (or end if empty)
lista_numerica.insert(0, 'Start')  # INSERT at specific index
del lista_numerica[-1]             # DELETE specific index
print(f"Final List: {lista_numerica}, Removed: {removed_value}")

# 3. Concatenation vs Extension
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b      # Returns a NEW list
list_a.extend(list_b)         # MODIFIES list_a in place
print(f"Extended A: {list_a}")

# 4. Memory Management (The '=' danger)
# For mutable types, '=' points to the same memory address!
l_origin = ['Luiz', 'Maria']
l_copy = l_origin.copy()      # Correct way to duplicate data
l_origin[0] = 'Changed'
print(f"Origin: {l_origin}, Copy: {l_copy}")
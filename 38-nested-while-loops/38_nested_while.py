"""
Topic: Nested While Loops
Focus: Executing a loop inside another loop to handle multi-dimensional data.
"""

# Repetitions
# while (enquanto)
# Nested loops allow us to work with rows and columns (matrix logic).

amount_rows = 5
amount_columns = 5

row = 1
while row <= amount_rows:
    column = 1
    
    while column <= amount_columns:
        print(f'{row=} {column=}')
        column += 1
        
    row += 1

print('The nested loop has finished.')
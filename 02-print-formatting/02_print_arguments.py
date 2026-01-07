"""
Topic: Print Function Arguments (sep and end)
Focus: Understanding how to format output and line breaks.
"""
# \r\n -> (CRLF - Carriage Return Line Feed): Padrão Windows.
# \n -> (LF - Line Feed): Padrão Linux/Mac.

# Argument 'sep' defines the separator between items
# Argument 'end' defines what happens at the end of the line

print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
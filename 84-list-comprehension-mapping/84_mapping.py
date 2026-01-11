"""
topic: List Comprehension - Mapping
focus: Transform each element of an iterable into a new value, keeping the same list length.
"""

products = [
    {'name': 'p1', 'price': 20},
    {'name': 'p2', 'price': 10},
    {'name': 'p3', 'price': 30},
]

# Mapping: Applying a 10% increase to all prices
# Logic: {**product} cpoies the dict, then we overwrite 'price'
new_products = [
    {**product, 'price': product['price'] * 1.1}
    for product in products
]

# Displaying the results

print("Original Products:")
print(*products, sep='\n')

print("\nMapped Products (10% Increase):")
print(*new_products, sep='\n')

# Example with conditional mapping:
# If price > 20, add 5% tax, otherwise keep original price
conditional_mapping = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
]

print("\nConditional Mapping (> 20 receives tax):")
print(*conditional_mapping, sep='\n')
# Largest Element in an Array
numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest Element:", largest)
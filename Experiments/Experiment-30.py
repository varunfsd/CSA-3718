# String Length Without Built-in len()
text = input("Enter a string: ")
count = 0

for ch in text:
    count += 1

print("String Length:", count)
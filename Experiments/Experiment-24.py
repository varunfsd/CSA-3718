# String Equality (Ignore Case)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1.lower() == s2.lower():
    print("Strings are Equal")
else:
    print("Strings are Not Equal")
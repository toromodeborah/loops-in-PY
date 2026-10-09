string = input("Please enter your own string :")

string2 = ('')
for r in string:
    string2 = r + string2

print("\nThe Original string = ", string)
print("The Reversed string = ", string2)
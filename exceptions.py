import sys


#x = int(input("x:"))
#y = int(input("y:"))
#result = x /y
#print(f"{x} divide by {y} = {result}")


#display error message for invalid input
try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

#display error for zero division.
try:
    result = x /y
except ZeroDivisionError:
    print("Cannot divide by zero.")
    sys.exit(1)

print(f"Division of {x} divided by {y} == {result}")
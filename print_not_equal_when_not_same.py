# Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 != num2:
    print(f"{num1} and {num2} are not equal numbers")
else:
    print("Sorry, they are equal!")
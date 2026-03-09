# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

no_decimal = num1 // num2
print(f"The quotient of {num1} and {num2} without decimal points is {no_decimal}")
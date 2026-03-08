# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"The quotient of {num1} and {num2} is {num1 / num2}")

# Method 2:
nums = [float(input("Enter first number: ")), float(input("Enter second number: "))]
print(f"The quotient of {nums[0]} and {nums[1]} is {nums[0] / nums[1]}")
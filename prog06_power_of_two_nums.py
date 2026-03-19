# Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{num1} to the power of {num2} is {num1 ** num2}")

# Method 2:
nums = [float(input("Enter first number: ")), float(input("Enter second number: "))]
print(f"{nums[0]} to the power of {nums[1]} is {nums[0] ** nums[1]}")
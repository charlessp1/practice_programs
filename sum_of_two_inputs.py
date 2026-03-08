# Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"The sum of {num1} and {num2} is {num1 + num2}")

# Method 2:
nums = [float(input("Enter first number: ")), float(input("Enter second number: "))]
print(f"The sum of {nums[0]} and {nums[1]} is {nums[0] + nums[1]}")
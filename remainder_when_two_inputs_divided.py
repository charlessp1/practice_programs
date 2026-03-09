# Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"The remainder of {num1} divided by {num2} is {num1 % num2}")

# Method 2:
nums = [float(input("Enter first number: ")), float(input("Enter second number: "))]
print(f"The remainder of {nums[0]} divided by {nums[1]} is {nums[0] % nums[1]}")
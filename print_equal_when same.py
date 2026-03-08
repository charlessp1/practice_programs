# Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# Method 1:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 == num2:
    print(f"{num1} and {num2} are equal numbers.")
else:
    print(f"{num2} and {num1} are not equal numbers.")

# Method 2:
nums = [float(input("Enter the first number: ")), float(input("Enter the second number: "))]
if nums[0] == nums[1]:
    print(f"{nums[0]} and {nums[1]} are equal numbers.")
else:
    print(f"{nums[0]} and {nums[1]} are not equal numbers.")
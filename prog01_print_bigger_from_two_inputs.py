# Create a program that ask user to input 2 numbers. Print the bigger number.

# Method 1: Basic Method
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is bigger than {num2}.")
else:
    print(f"{num2} is bigger than {num1}.")

# Method 2:
nums = [float(input("Enter the first number: ")), float(input("Enter the second number: "))]
print(f"{max(nums)} is bigger than {min(nums)}.")
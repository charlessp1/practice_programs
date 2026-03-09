# Create a program that ask user to input 2 numbers. Print the smaller number.

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num2} is smaller than {num1}")

# Method 2:
nums = [float(input("Enter first number: ")), float(input("Enter second number: "))]
print(f"{min(nums)} is smaller than {max(nums)}")
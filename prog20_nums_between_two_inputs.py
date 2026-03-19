# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Method 1:
between = []
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

for num in range(int(num1) + 1, int(num2)):
    between.append(num)
print(*between, sep=',')

# Method 2:
nums = [float(input("Enter first number: ")), float(input("Enter second number: "))]
num_between = [num for num in range(int(nums[0]) + 1, int(nums[1]))]
print(*num_between, sep=',')
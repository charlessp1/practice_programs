# Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# Method 1
nums = 0
first_num = float(input("Enter first number: "))
for i in range(9, 0, -1):
    num = float(input(f"Enter {i} more numbers: "))
    nums += num
print(f"{first_num} minus {nums} is {first_num - nums}")

# Method 2
first_number = float(input("Enter first number: "))
nums = [float(input(f"Enter {i} more numbers: ")) for i in range(9, 0, -1)]
print(f"{first_number} minus {sum(nums)} is {first_number - sum(nums)}")
# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Method 1:
nums = []
no_dups = []
for i in range(10, 0, -1):
    number = float(input(f"Enter {i} numbers: "))
    nums.append(number)
for num in nums:
    if nums.count(num) == 1:
        no_dups.append(num)
print(*no_dups, sep=', ')
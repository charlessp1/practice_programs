# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Method 1:
nums = [float(input(f"Enter {i} number: ")) for i in range(10, 0, -1)]
print(*[num for num in nums if nums.count(num) > 1], sep=',')
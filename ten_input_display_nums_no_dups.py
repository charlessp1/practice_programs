# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Method 1:
nums = [float(input(f"Enter {i} numbers: ")) for i in range(10, 0, -1)]
print([num for num in nums if nums.count(num) == 1])
# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#Method 1:
nums = [float(input(f"Enter {i} numbers: ")) for i in range(10, 0, -1)]
print(*dict.fromkeys(nums), sep=',')
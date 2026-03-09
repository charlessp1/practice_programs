# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# Method 1:
nums = []
for num in range(101):
    if num % 10 and num % 5 != 0:
        nums.append(num)
print(*nums, sep=',')

# Method 2:
nums = [num for num in range(101) if num % 10 and num % 5 !=0]
print(*nums, sep=',')
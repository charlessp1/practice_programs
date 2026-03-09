# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# Method 1:
nums_w_zero = []
for num in range(0, 101):
    if num % 10 == 0:
        nums_w_zero.append(num)
print(*nums_w_zero, sep=',')

# Method 2:
print(*range(0, 101, 10))

# Method 3:
nums = [num for num in range(0, 101)]
print(*[num for num in nums if num % 10 == 0])
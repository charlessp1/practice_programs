# Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

# Method 1:
nums = []
for i in range(101):
    if i % 2 == 0:
        nums.append(i)
print(*nums, sep=',')

#
# Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# Method 1:
odds = []
for num in range(0, 101):
    if num % 2 != 0:
        odds.append(num)
print(*odds, sep=',')
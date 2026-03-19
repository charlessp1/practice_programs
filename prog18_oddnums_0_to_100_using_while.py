# Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# Method 1:
count = 0
odds = []
while count < 100:
    count += 1
    if count % 2 != 0:
        odds.append(count)
print(*odds, sep=',')
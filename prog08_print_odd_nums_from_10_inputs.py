# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Method 1:
nums = []
for i in range (1, 11):
    num = float(input(f"{i}. Enter a number: "))
    if num % 2 != 0: nums.append(num)
print(f"{len(nums)} of the numbers you entered are odd numbers")

# Method 2:
nums = [float(input(f"{i}. Enter a number: ")) for i in range(1, 11)]
print(f"{len([num for num in nums if num % 2 != 0])} of the numbers are odd numbers")
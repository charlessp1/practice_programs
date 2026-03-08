# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#Method 1:
nums = 0
for i in range(1, 11):
    num = float(input(f"{i}. Enter a number: "))
    nums += num
print(f"The sum of all ten numbers is {nums}")

# Method 2:
nums = []
for i in range (1, 11):
    num = float(input(f"{i}. Enter a number: "))
    nums.append(num)
print(f"The sum of all ten numbers is {sum(list(map(float, nums)))}")
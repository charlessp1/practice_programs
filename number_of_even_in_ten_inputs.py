# Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Method 1:
nums = []
for num in range(10):
    number = float(input("Enter a number: "))
    if number % 2 == 0:
        nums.append(num)
print(f"{len(nums)} of numbers you entered are even numbers")

# Method 2:
nums = [float(input("Enter a number: ")) for i in range(10)]
evens = [num for num in nums if num % 2 == 0]
print(len(evens), "of the numbers you entered are even numbers")
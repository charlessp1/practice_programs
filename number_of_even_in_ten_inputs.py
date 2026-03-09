# Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Method 1:
nums = []
for num in range(10):
    number = float(input("Enter a number: "))
    if number % 2 == 0:
        nums.append(num)
print(f"{len(nums)} of numbers you entered are even numbers")
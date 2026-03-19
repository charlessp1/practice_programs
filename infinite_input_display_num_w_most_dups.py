# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Method 1:
nums = []
most_dups = 0
num_highest = None
while True:
    try:
        num = float(input("Enter a number: "))
        nums.append(num)
        if nums.count(num) > most_dups:
            most_dups = nums.count(num)
            num_highest = num
    except ValueError:
        print("Invalid input")
        print(f"The number with most duplicates is {num_highest} with {most_dups} duplicates")
        break
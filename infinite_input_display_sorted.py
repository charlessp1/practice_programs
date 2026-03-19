# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# Method 1:
nums = []
while True:
    try:
        num = float(input("Enter a number: "))
        nums.append(num)
    except ValueError:
        print("Invalid input")
        print(*sorted(nums), sep=',')
        break
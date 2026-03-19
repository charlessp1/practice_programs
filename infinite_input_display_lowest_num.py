# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# Method 1:
nums = []
while True:
    try:
        num = float(input("Enter a number: "))
        nums.append(num)
    except ValueError:
        print("Invalid input")
        print(f"The lowest number is {min(nums)}")
        break
# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# Method 1:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

no_decimal = num1 // num2
print(f"The quotient of {num1} and {num2} without decimal points is {int(no_decimal)}")

# Method 2:
nums = [float(input("Enter first number: ")), float(input("Enter second number: "))]
print(f"The quotient of {nums[0]} and {nums[1]} rounded off is {round(nums[0] / nums[1])}")
# Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# Method 1:
name = str(input("Enter your full name with several spaces in front: "))
print(name.strip())
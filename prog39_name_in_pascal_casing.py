# Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# Method 1:
name = str(input("Enter your name: "))
print(name.title().replace(" ", ""))

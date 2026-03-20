# Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# Method 1:
name = str(input("Enter your name in improper casing: "))
print(name.lower().replace(" ","_"))
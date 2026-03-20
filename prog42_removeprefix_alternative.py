# removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# Method 1:
name = str(input("Enter your full name: "))
remove = str(input("Enter the string you want to remove: "))
if name.startswith(remove):
    name = name[len(remove):]
else:
    name = name
print(name)
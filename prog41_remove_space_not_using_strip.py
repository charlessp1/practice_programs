# lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Method 1:
name = str(input("Enter your name with multiple spaces in front: "))
for i in range(len(name)):
    if name[i] != ' ':
        name = name[i:]
        break
print(name)
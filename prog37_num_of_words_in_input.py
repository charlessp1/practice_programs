# Create a program that ask the user to input a complete statement. Print the number of words in the input.

#Method 1:
statement = str(input("Enter a statement: "))
print(len(statement.split()))
# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks on the same line
    for _ in range(size):
        print("*", end="")
    # After each row, print a newline character to move to the next line
    print()
    row += 1

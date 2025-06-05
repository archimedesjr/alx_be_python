rows = 5  # You can change this to any number you like

row = 1
while row <= rows:
    # Print spaces
    spaces = 1
    while spaces <= (rows - row):
        print(" ", end="")
        spaces += 1

    # Print asterisks
    stars = 1
    while stars <= (2 * row - 1):
        print("*", end="")
        stars += 1

    print()  # Move to the next line after each row
    row += 1

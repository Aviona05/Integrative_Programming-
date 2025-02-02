def pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")  # Print leading spaces
        for j in range(1, i + 1):
            print(j, end="")  # Print numbers without extra spaces
        print()  # Move to the next line

# Define and call the function
rows = 5
pattern(rows)

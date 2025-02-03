def pattern(rows):
    i = 1  # Start with 1
    while i <= rows:
        if i % 2 != 0:  # Print only for odd numbers
            print(" " * ((rows - i) // 2), end="")  # Adjust leading spaces
            j = 0
            while j < i:
                print(i, end="")  # Print 'i' i times
                j += 1
            print()  # Move to the next line
        i += 1  # Increment i

# Call the function
pattern(7)

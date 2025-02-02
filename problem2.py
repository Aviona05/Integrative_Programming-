def num_of_Digits(string):
    count = 0
    for ch in string:
        if ch.isdigit():
            count += int(ch)
    return count

inp_string = input("Enter a string with digits: ")
result = num_of_Digits(inp_string)

print("The sum of the digits in the string is:", result)
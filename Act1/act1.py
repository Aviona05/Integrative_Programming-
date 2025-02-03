no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))
no3 = float(input("Enter third number: "))

# Finding the highest number
if no1 > no2 and no1 > no3:
    highest = no1
elif no2 > no1 and no2 > no3:
    highest = no2
else:
    highest = no3

print(f"The highest number is: {highest}")

# Finding middle and lowest numbers
if highest == no1:
    if no2 > no3:
        middle = no2
        lowest = no3
    else:
        middle = no3
        lowest = no2
elif highest == no2:
    if no1 > no3:
        middle = no1
        lowest = no3
    else:
        middle = no3
        lowest = no1
else:
    if no1 > no2:
        middle = no1
        lowest = no2
    else:
        middle = no2
        lowest = no1

# Displaying numbers in descending order
print(f"The numbers in descending order are: {highest}, {middle}, {lowest}")

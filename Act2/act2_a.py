no1= int(input("Enter the first number: "))
no2= int(input("Enter the second number: "))

total = 0
no = no1
while no <= no2:
    total += no
    no += 1

print("The sum of all the numbers between", no1, "and", no2, "is", total)
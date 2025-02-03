no = int(input("Enter a number: "))
if no > 1:
    is_prime = True
    for i in range(2, no):
        if no % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{no}, is a prime number")
    else:
        print(f"{no}, is not a prime number")
else:
    print(f"{no}, is not a prime number")
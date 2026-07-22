n = int(input("Enter the value of n: "))

if n <= 1:
    print("NOT PRIME")
elif n == 2:
    print("PRIME")
elif n % 2 == 0:
    print("NOT PRIME")
else:
    is_prime = True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("PRIME")
    else:
        print("NOT PRIME")

user = int(input("Please enter an integer: "))
if user <= 1:
    print(f"Number {user} is not a prime number.")
else:
    prime = True
    for i in range(2, user):
        if user % i == 0:
            prime = False
    if prime:
        print(f"Number {user} is a prime number.")
    else:
        print(f"Number {user} is not a prime number.")

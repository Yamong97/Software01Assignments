import random

random_integer = random.randint(1,10)

user = float(input("Enter a random integer between 1 and 10: "))

while user != random_integer:
    if user > random_integer:
        print("Too high!")
    elif user < random_integer:
        print("Too low!")

    user = float(input("Enter a random integer between 1 and 10: "))

print("correct!")

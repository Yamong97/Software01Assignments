import random

num_dice = int(input("How many dice to roll?: "))

total = 0

for i in range(num_dice):
    dice = random.randint(1,6)
    print(f"Dice {i+1}: {dice}")
    total += dice

print(f"The sum of the numbers is: {total}")
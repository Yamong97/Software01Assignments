import random

def dice_roll(sides):
    random_roll = random.randint(1, sides)
    return random_roll

def main():
    sides = 0
    sides = int(input("Number of sides roll-playing dice: "))
    if sides <=1:
        print("You can't roll one and less than one.")

    result = 0

    while result != sides:
        result = dice_roll(sides)
        print(f"The number of sides: {result}")

    print("Thank you for playing! You have the maximum number of roll-playing dice.")

main()
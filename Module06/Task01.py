import random

def dice_roll():
    random_roll = random.randint(1, 6)
    return random_roll

def main():
    result_roll = dice_roll()

    while result_roll != 6:
        print(f"The result roll is {result_roll}")
        result_roll = dice_roll()
    print(f"The result roll is 6. Congratulations!")

main()
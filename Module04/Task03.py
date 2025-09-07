Numbers= []

user = input("Enter a number or press enter to equit: ")

while user != "":
    number = float(user)
    Numbers.append(number)

    user = input("Enter a number or press enter to equit: ")

if len(Numbers) > 0 :

    smallest_number = min(Numbers)
    largest_number = max(Numbers)

    print(f"The smallest number is: {smallest_number}")
    print(f"The largest number is: {largest_number}")

else:
    print("No numbers found!")
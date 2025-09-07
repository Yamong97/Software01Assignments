numbers =[]

user = input("Please enter number or input empty string to quit: ")

while user != "":
    number = float(user)
    numbers.append(number)
    user = input("Please enter number or input empty string to quit: ")

numbers.sort(reverse=True)

greatest_numbers = numbers [:5]

print(f"The five greatest numbers are: {greatest_numbers:}.")
for greatest_number in numbers:
    print(f"* {greatest_number: .2f}")
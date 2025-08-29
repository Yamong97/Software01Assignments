cm_to_in = 2.54

inches = float(input("Enter the inches: "))

while inches>=0:
    centimeters = inches + 2.54
    print(f"{inches} inches is {centimeters} centimeters.")

    inches = float(input("Enter the inches: "))

print ("Program end!")

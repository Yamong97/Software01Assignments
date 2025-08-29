zander_length = float(input("Enter length of zander: "))
size_limit = 42

if zander_length < size_limit:
    size_difference = size_limit - zander_length
    print(f"The zander is {size_difference} centimeters below the size limit and please release the fish back in the sea!")

else:
    print("Please keep the fish!")
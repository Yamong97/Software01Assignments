Cabin_class = input("Please enter the class (LUX, A, B, C): ")

if Cabin_class == "LUX":
    print("upper-desk class with a balcony.")

elif Cabin_class == "A":
    print("above the car deck, equipped with a window.")

elif Cabin_class == "B":
    print("windowless cabin above the car deck.")

elif Cabin_class == "C":
    print("windowless cabin below the car deck.")

else:
    print("Invalid cabin class.")

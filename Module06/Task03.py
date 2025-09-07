def the_number_of_gasoloine_in_USA(gallons):
    return gallons *3.78541

def main ():
    gallons = float(input("Please enter the volume of gallons: "))

    while gallons >= 0:
        liters = the_number_of_gasoloine_in_USA(gallons)
        print(f"The number of gasoline in USA is : {liters: .2f} liters.")
        gallons = float(input("Please enter the volume of gallons: "))

    print("Sorry! This is not a valid amount of gallons.")

main ()

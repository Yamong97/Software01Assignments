import math

def unit_price_of_square_meter (parameter_cm, price_Euro):
    radius_meter_square = (parameter_cm /2)/100
    area_meter_square = math.pi*(radius_meter_square**2)
    return price_Euro/area_meter_square

def main():
    D_pizza1 = float(input("Please enter the diameter of the pizza1: "))
    P_pizza1 = float(input("Please enter the price of the pizza1: "))
    Unit_price1 = unit_price_of_square_meter(D_pizza1, P_pizza1)

    D_pizza2 = float(input("Please enter the diameter of the pizza2: "))
    P_pizza2 = float(input("Please enter the price of the pizza2: "))
    Unit_price2 = unit_price_of_square_meter(D_pizza2, P_pizza2)

    print(f"The unit price of pizza1 is : {Unit_price1: .2f} per m². ")
    print(f"The unit price of pizza2 is : {Unit_price2: .2f} per m². ")

    if Unit_price1 > Unit_price2:
        print("The pizza 1 is better value for money.")
    elif Unit_price1 < Unit_price2:
        print("The pizza 2 is better value for money.")
    else:
        print("Both pizzas are same value of money.")

main()




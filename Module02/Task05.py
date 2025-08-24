
talents = int(input("Please enter the talents: "))
pounds = int(input("Please enter the pounds: "))
lots = float(input("Please enter the lots: "))

Total_grams = (talents*20*32*13.3) + (pounds*32*13.3) + (lots*13.3)

kilograms = Total_grams / 1000
grams = Total_grams % 1000

print(f"The weight in modern unit is {kilograms} Kilograms and {grams} Grams.")
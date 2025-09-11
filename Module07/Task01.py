seasons = ("Spring", "Summer", "Autumn", "Winter")

month = int(input("Please enter a number of month (1 to 12): "))

if month in (12,1,2):
    season = f"The season is {seasons[3]}."
elif month in (3,4,5):
    season = f"The season is {seasons[0]}."
elif month in (6,7,8):
    season = f"The season is {seasons[1]}."
elif month in (9,10,11):
    season = f"The season is {seasons[2]}."
else:
    season = "Sorry! Invalid month!"
print(season)



gender = input("Please enter gender: ")

hemoglobin = float(input("Please enter hemoglobin: "))

if gender == "Female":
    if hemoglobin < 117:
        print("The hemoglobin value for Female is Low!")
    elif hemoglobin <= 155:
        print("The hemoglobin value for Female is normal!")
    else:
        print("The hemoglobin value for Female is High!")

if gender == "Male":
    if hemoglobin < 134:
        print("The hemoglobin value for Male is Low!")
    elif hemoglobin <= 167:
        print("The hemoglobin value for Male is normal!")
    else:
        print("The hemoglobin value for Male is High!")
names = set()

name = input("Please enter name or empty string: ")

while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Please enter name or empty string: ")

print("The list of the names are the following: ")

for i in names:
    print(i)



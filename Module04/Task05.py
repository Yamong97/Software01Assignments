username = "python"
password = "rules"

total_attempts = 0


while total_attempts < 5:
    Username = input("Please enter your username: ")
    Password = input("Please enter your password: ")

    if Username != username or Password != password:
        print("Please enter user and password again")
        total_attempts += 1

    else:
        print("Welcome")
        break

if total_attempts == 5:
    print("Access Denied")


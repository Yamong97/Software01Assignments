from classes.car import Car

car = Car("ABC-123", 142)

print(f"Registration number: {car.registration_number}")

car.accelerate(60)
car.travelled_distance = 2000
car.drive(1.5)

print(f"The current speed of the cur is {car.current_speed} km.")
print(f"The travelled distance is {int(car.travelled_distance)} km.")
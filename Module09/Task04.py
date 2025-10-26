import random
from classes.car import Car

car_list= []
for i in range (10):
    max_speed = random.randint(100,200) 
    car = Car("ABC-" + str(i+1), max_speed)
    car_list.append(car)

race_distance = 0
while race_distance < 10000:
    for car in car_list:
        change_in_speed = random.randint(-10, 15)
        car.accelerate(change_in_speed)
        car.drive(1)

    race_distance += car.travelled_distance

print(f"|{'Registration':<13} | {'MaxSpeed':<10} | {'CurSpeed':<10} | {'Distance':<8}|")
print("-" * 52)
for car in car_list:
    print(f"|{car.registration_number:<13} | {car.max_speed:<10} | {car.current_speed:<10} | {car.travelled_distance:<8}|")



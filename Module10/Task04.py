import random

class Car:
    def __init__(self, new_registration_number, new_max_speed):
        self.registration_number = new_registration_number
        self.max_speed = new_max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, value):
        self.current_speed = self.current_speed + value

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        #use time and current speed to calculate
        self.travelled_distance += self.current_speed * hours

    def change_in_speed(self):
        self.current_speed += random.randint(-10, 15)
        self.accelerate(self.current_speed)
        self.drive(1)

class Race:
    def __init__(self, name, distance_in_km, car_list):
        self.name = name
        self.distance_in_km = distance_in_km
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.change_in_speed()

    def print_status(self):
        print(f"{'Car':<10} {'Travelled_Distance':<15}")
        print(f"-" * 32)
        for car in self.car_list:
            print(f"{car.registration_number:<10} {car.travelled_distance:<15}")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance_in_km:
                return True

        return False

car_list= []
for i in range (10):
    max_speed = random.randint(100, 200)
    car = Car("Car " + str(i+1), max_speed)
    car_list.append(car)

race = Race("Grand Demolition Derby", 8000, car_list)

hours = 0
while not race.race_finished():
    hours += 1
    race.hour_passes()
    if hours % 10 == 0:
        print(f"\nCurrent Status after {hours} hours passed:")
        race.print_status()

print(f"\nFinal Status after {hours} hours passed:.")
race.print_status()

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        Car.__init__(self, registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        Car.__init__(self, registration_number, max_speed)
        self.tank_volume = tank_volume

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

electric.current_speed = 150
gasoline.current_speed = 120

electric.drive(3)
gasoline.drive(3)

print("Electric car distance:", electric.travelled_distance, "km")
print("Gasoline car distance:", gasoline.travelled_distance, "km")
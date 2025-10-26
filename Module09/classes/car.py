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


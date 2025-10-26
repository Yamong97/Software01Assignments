class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = 0

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Elevator moved up to floor {self.current_floor}.")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Elevator moved down to floor {self.current_floor}.")
        if self.current_floor == self.bottom_floor:
            print(f"Elevator is at Ground Floor now.")


    def go_to_floor(self, destination):

        while self.current_floor < destination:
            self.floor_up()

        while self.current_floor > destination:
            self.floor_down()


class Building:

    def __init__(self, num_bottom, num_top, num_elevator):
        self.elevators = []
        for i in range(num_elevator):
            self.elevators.append(Elevator(num_bottom, num_top))

    def run_elevator(self, num_of_elevator, destination_floor):
        elevator = self.elevators[num_of_elevator]
        self.num_of_elevator = num_of_elevator + 1
        print(f"\nElevator number {self.num_of_elevator} goes to floor: {destination_floor}")
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFire Alarm! All elevators need to go ground floor.")
        i = 1
        for elevator in self.elevators:

            print(f"\nElevator {i} is currently at floor {elevator.current_floor}.")
            elevator.go_to_floor(elevator.bottom_floor)
            i += 1

building = Building(0, 8, 2)
building.run_elevator(0, 8)
building.run_elevator(1, 4)
building.fire_alarm()

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = 0
        print(f"Elevator is at floor {self.current_floor} now.")

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Elevator moved up to floor {self.current_floor}.")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Elevator moved down to floor {self.current_floor}.")
        if self.current_floor == self.bottom_floor:
            print(f"Elevator is at Ground Floor again.")


    def go_to_floor(self, destination):

        while self.current_floor < destination:
            self.floor_up()

        while self.current_floor > destination:
            self.floor_down()

h = Elevator(0,12)
h.go_to_floor(5)
h.go_to_floor(0)



from classes.car import Car

car1 = Car('ABC-123', 142)

print(f"""Registration: {car1.registration_number}
Max speed: {car1.max_speed}
Current speed: {car1.current_speed}
Travelled distance: {car1.travelled_distance}""")
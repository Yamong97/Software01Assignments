import random

N = int(input("Please enter total random points: "))

points_in_circle = 0
total_points = 0

while total_points < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 <1:
        points_in_circle += 1

    total_points += 1

pi = 4*points_in_circle/N

print(f"There are {points_in_circle} points in the circle.")
print(f"The approximation of the value of pi is {pi}.")

import random

N = int(input("Please enter the total number of total random points: "))

points_in_circle = 0
total_points = 0

while total_points < N:
    a = random.uniform(-1,1)
    b = random.uniform(-1,1)

    if a**2 + b**2 <1:
        points_in_circle += 1

        total_points += 1

pi = 4*points_in_circle/N

print(f"The approximation of the value of pi is {pi}")

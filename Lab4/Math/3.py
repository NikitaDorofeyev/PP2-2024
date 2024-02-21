# Program to calculate the area of a regular polygon

import math

num_sides = int(input("Number of sides: "))
side_length = float(input("The length of a side: "))

area = round((num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides)), 3)

print(f"The area of the polygon is: {area}")
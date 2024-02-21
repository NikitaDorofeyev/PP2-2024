# Program to calculate the area of a trapezoid

import math

def trapezoid_area(height, base1, base2):
    area = (base1+base2) * height / 2
    return area

height = float(input("Height: "))
b_firstValue = float(input("Base, first value: " ))
b_secondValue = float(input("Base, second value: "))

area = trapezoid_area(height, b_firstValue, b_secondValue)

print(f"The area of a trapezoid is: {area}")

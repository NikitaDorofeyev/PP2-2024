import math

def volumeOfSphere(radius):
    volume = 4/3 * math.pi * radius**3
    return volume

radius = int(input())

result = round(volumeOfSphere(radius), 3)

print(f"The volume of a sphere is {result}")
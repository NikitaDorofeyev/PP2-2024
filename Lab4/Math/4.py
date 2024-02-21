# Program to calculate the area of a parallelogram

def parallelogram_area(base, height):
    return base*height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base, height)

print(f"The are of a parallelogram is: {area}")




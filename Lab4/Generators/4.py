# Program that yield the square of all numbres from (a) to (b).

def generate_squares(a, b):
    while a <= b:
        yield a ** 2
        a += 1

a = int(input("Start: "))
b = int(input("End: "))

squares = generate_squares(a, b)

for square in squares:
    print(square)
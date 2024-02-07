import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
x1 = int(input())
y1 = int(input())
p1 = Point(x1, y1)

x2 = int(input())
y2 = int(input())
p2 = Point(x2, y2)

p1.show()

p1.move(1, -2)

p1.show()

distance = p1.dist(p2)

print("Distance:", distance)
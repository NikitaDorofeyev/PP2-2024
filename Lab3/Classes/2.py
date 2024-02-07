class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class _Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length **2

length = int(input())

square = _Square(length)

print(square.area())

    
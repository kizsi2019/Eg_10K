class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length ** 2

square = Square(5)
print("Perimeter:", square.perimeter())
print("Area:", square.area())

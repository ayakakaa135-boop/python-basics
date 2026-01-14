from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other):

        return (self.x**2 + self.y**2 + self.z**2) < (other.x**2 + other.y**2 + other.z**2)

    def __str__(self):
        return f"The numbers are: {self.x}, {self.y}, {self.z}"


p1 = Point(1, 2, 3)
p2 = Point(2, 2, 2)
p3 = Point(1, 2, 3)

print(p1 == p3)
print(p1 < p2)
print(p1 > p2)
print(p1 <= p2)
print(p1 >= p3)

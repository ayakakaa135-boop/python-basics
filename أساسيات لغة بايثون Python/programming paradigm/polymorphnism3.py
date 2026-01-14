from functools import total_ordering

@total_ordering

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __gt__(self, other):
        self_length_sq = self.x ** 2 + self.y ** 2 + self.z ** 2
        other_length_sq = other.x ** 2 + other.y ** 2 + other.z ** 2

        return self_length_sq > other_length_sq

    def __lt__(self, other):
        self_length_sq = self.x ** 2 + self.y ** 2 + self.z ** 2
        other_length_sq = other.x ** 2 + other.y ** 2 + other.z ** 2

        return self_length_sq < other_length_sq

    def __gt__(self, other):
        self_length_sq = self.x ** 2 + self.y ** 2 + self.z ** 2
        other_length_sq = other.x ** 2 + other.y ** 2 + other.z ** 2

        return self_length_sq > other_length_sq

    def __lt__(self, other):
        self_length_sq = self.x ** 2 + self.y ** 2 + self.z ** 2
        other_length_sq = other.x ** 2 + other.y ** 2 + other.z ** 2

        return self_length_sq < other_length_sq

    def _length_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def __gt__(self, other):
        return self._length_squared() > other._length_squared()

    def __lt__(self, other):
        return self._length_squared() < other._length_squared()
p1 = Point(1, 2, 3)
p2 = Point(2, 2, 2)
p3 = Point(1, 2, 3)
print(f"p1 >= p3: {p1 >= p3}")
print(f"p2 <= p1: {p2 <= p1}")
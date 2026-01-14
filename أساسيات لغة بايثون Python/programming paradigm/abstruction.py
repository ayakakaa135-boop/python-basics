from abc import ABC ,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def info(self):
        return 'shape has a defined area'



class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return( self.base *self.height)/2



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2 *3.14


square=Square(4)
print(square.area())
triangle=Triangle(2,3)
print(triangle.area())
circle=Circle(3)
print(circle.area())
print(circle.info())
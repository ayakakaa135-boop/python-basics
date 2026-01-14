class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return print(self.x+other.x,self.y+other.y,self.z+other.z)

    def __str__(self):
        return f"The numbers are: {self.x}, {self.y}, {self.z}"
p=Point(1,2,3)
"""print(dir(int))"""
print(p)
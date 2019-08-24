class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point:({self.x},{self.y},{self.z})'
    
    def __repr__(self):
        return (self.x,self.y,self.z)

p1 = Point(3, 5, 7)

print(p1)

class Circle:

    def __init__(self, center, r):
        self.center = center
        self.r = r

    def get_area(self):
        area = 3.14 * self.r * self.r
        return area
    
    def get_perimeter(self):
        perimeter = 3.14 * 2 * self.r
        return perimeter

    def get_center(self):
        return self.center

    def __str__(self):
        return f'Circle:({self.center.x},{self.center.y}),r:r'

p2 = Point(4, 6, 7)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
print(c2)
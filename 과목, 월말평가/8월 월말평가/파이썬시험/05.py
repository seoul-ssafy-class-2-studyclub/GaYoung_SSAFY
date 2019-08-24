# 파일명을 변경하지 마시오.
# 아래에 Point 클래스 및 Rectangle 클래스를 작성하시오.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def get_area(self):
        if self.p1.x > self.p2.x and self.p1.y > self.p2.y: 
            result = (self.p1.x - self.p2.x) * (self.p1.y - self.p2.y)
        elif self.p1.x > self.p2.x and self.p1.y < self.p2.y: 
            result = (self.p1.x - self.p2.x) * (self.p2.y - self.p1.y)
        elif self.p1.x < self.p2.x and self.p1.y > self.p2.y: 
            result = (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)
        elif self.p1.x < self.p2.x and self.p1.y < self.p2.y: 
            result = (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)
        return result


    def get_perimeter(self):
        if self.p1.x > self.p2.x and self.p1.y > self.p2.y: 
            result = 2 * (self.p1.x - self.p2.x) + 2 * (self.p1.y - self.p2.y)
        elif self.p1.x > self.p2.x and self.p1.y < self.p2.y: 
            result = 2 * (self.p1.x - self.p2.x) + 2 * (self.p2.y - self.p1.y)
        elif self.p1.x < self.p2.x and self.p1.y > self.p2.y: 
            result = 2 * (self.p2.x - self.p1.x) + 2 * (self.p1.y - self.p2.y)
        elif self.p1.x < self.p2.x and self.p1.y < self.p2.y: 
            result = 2 * (self.p2.x - self.p1.x) + 2 * (self.p2.y - self.p1.y)
        return result


    def is_square(self):
        if abs(self.p1.x - self.p2.x) and abs(self.p1.y - self.p2.y):
            ans = True
        else:
            ans = False
        return ans










# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    p1 = Point(1, 3)
    p2 = Point(3, 1)
    r1 = Rectangle(p1, p2)
    print(r1.get_area())
    print(r1.get_perimeter())
    print(r1.is_square())
    p3 = Point(3, 7)
    p4 = Point(6, 4)
    r2 = Rectangle(p3, p4)
    print(r2.get_area())
    print(r2.get_perimeter())
    print(r2.is_square())

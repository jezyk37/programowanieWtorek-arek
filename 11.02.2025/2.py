# inicjalizer__init__(self) self oznacza ze pracujemy na jednej instancji klasy
#referencja do instancji

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

p1 = Point()
print(p1.x,p1.y)

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = Point1(4,6)
p3 = Point1(0)
p4 = Point(1,1)
print(p2.x,p2.y)
print(p3.x,p3.y)
print(p4.x,p4.y)
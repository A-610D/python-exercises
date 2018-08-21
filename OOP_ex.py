#class Apple():
#    def __init__(self, w, d, cl, cn):
#        self.weigth = w
#        self.diameter = d
#        self.color = cl
#        self.country = cn

#import math
#class Circle():
#    def __init__(self, r):
#        self.radius = r
#    def area(self):
#        print(self.radius*self.radius*math.pi)

#cir1 = Circle(10)
#cir1.area()

#3. Создайте класс Triangle с методом area, подсчитывающим и возвращающим
#площадь треугольника. Затем создайте объект Triangle, вызовите в
#нем area и выведите результат.

#import math

#class Triangle():
#    def __init__(self, a, b, c):
#        self.a = a
#        self.b = b
#        self.c = c
#    def area(self):
#        p = (self.a+self.b+self.c)/2
#        s = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
#        print(s)

#trg1 = Triangle(1,1,1.41)
#trg1.area()

#4. Создайте класс Hexagon с методом calculate_perimeter, подсчитыва-
# ющим и возвращающим периметр шестиугольника. Затем создайте объект
# Hexagon, вызовите в нем calculate_perimeter и выведите результат

class Hexagon():
    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.sides = [a1,a2,a3,a4,a5,a6]
    def calculate_perimeter(self):
        per = 0
        for s in self.sides:
            per +=s
        print(per)

hex = Hexagon(1,2,1,2,1,2)
hex.calculate_perimeter()
        

# 1. Создайте классы Rectangle и Square с методом calculate_perimeter,
# вычисляющим периметр фигур, которые эти классы представляют. Создайте
# объекты Rectangle и Square вызовите в них этот метод.

class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print('Я - фигура')
        
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calculate_perimeter(self):
        p = (self.a+self.b)*2
        print('Rect: ' + str(p))
        return p

class Square(Rectangle):
    def __init__(self, a):
        self.a = a
        self.b = a

    def change_size(self, d):
        self.a = self.a + d
        self.b = self.b + d

#rect = Rectangle(2,3)
#rect.calculate_perimeter()

#sq = Square(4)
#sq.calculate_perimeter()

#2. В классе Square определите метод change_size, позволяющий передавать
#ему число, которое увеличивает или уменьшает (если оно отрицательное)
#каждую сторону объекта Square на соответствующее значение.

#sq = Square(4)
#sq.calculate_perimeter()        
#sq.change_size(1)
#sq.calculate_perimeter()
#sq.change_size(-2)
#sq.calculate_perimeter()

#3. Создайте класс Shape. Определите в нем метод what_am_i, который при вызове
#выводит строку "Я - фигура". Измените ваши классы Rectangle и
#Square из предыдущих заданий для наследования от Square, создайте объекты
#Square и Rectangle и вызовите в них новый метод.

#rect = Rectangle(2,3)
#sq = Square(4)
#rect.what_am_i();
#sq.what_am_i();

#Создайте классы Horse и Rider. Используйте композицию, чтобы смоделировать
#лошадь с всадником на ней.

#class Horse():
#    def __init__(self, a):
#        self.a = a        

#class Rider():
#    def __init__(self, a):
#        self.a = a        

#class Horseman():
#    def __init__(self):
#        self.horse = Horse(1);
#        self.rider = Rider(2);

#hm = Horseman()
#print(hm.horse.a)
#print(hm.rider.a)

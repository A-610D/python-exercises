#1. Добавьте переменную square_list в класс Square так, чтобы всякий раз,
#когда вы создаете новый объект Square, он добавлялся в список.


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
    square_list = []
    
    def __init__(self, a):
        self.a = a
        self.b = a
        self.square_list.append((a,a))

    def change_size(self, d):
        self.a = self.a + d
        self.b = self.b + d

    def __repr__(self):
        return '{} на {} на {} на {}'.format(self.a, self.a, self.a, self.a)

#s1=Square(2)
#s2=Square(3)
#s3=Square(7)
#print(s1.square_list)

# 2. Измените класс Square так, чтобы когда вы выводите объект Square, выводилось
#сообщение с длинами всех четырех сторон фигуры. Например, если
#вы создадите квадрат при помощи Square(29) и осуществите вывод, Python
#должен вывести строку 29 на 29 на 29 на 29.

#s3=Square(259)
#print(s3)

#3. Напишите функцию, которая принимает два объекта в качестве параметров
#и возвращает True, если они являются одним и тем же объектом, и False в
#противном случае.

def Comp(Obj1, Obj2):
    return Obj1 is Obj2

s3 = Square(29)
s4 = Square(30)
s3=s4
print(Comp(s3,s4))

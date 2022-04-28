"""Задание 2
Создайте класс для подсчета площади геометрических
фигур. Класс должен предоставлять функциональность
для подсчета площади треугольника по разным формулам,
площади прямоугольника, площади квадрата, площади
ромба. Методы класса для подсчета площади должны
быть реализованы с помощью статических методов. Также
класс должен считать количество подсчетов площади и
возвращать это значение с помощью статического метода."""
from Lesson33v import GeometryValidation as GV

# class Area:
#     figure = ''
#     side_1 = float()
#     side_2 = float()
#     side_3 = float()
#     side_4 = float()
#
#     def __init__(self, figure, side_1, side_2=side_1, side_3=side_1):
#         self.side_1 = side_1
#         self.side_2 = side_2
#         self.side_3 = side_3
#
#     @staticmethod
#     def area_triangle(self):
#         pass
#     @staticmethod
#     def area(self):
#         area = self.side_1 * self.side_2
#         print(area)

class Geomerty(GV):
    figure = str()#name
    sides = list()#3-8

    def __init__(self,*sides):
        self.count = len(sides)
        self.sides = sides
        self.s = 1

    @staticmethod
    def area(self):
        if self.count == 3:
            for side in self.sides:
                self.s = self.s * side
            return self.s
        elif self.count == 4:
            for side in self.sides:
                self.s = self.s * side
            return self.s

a = Geomerty(3,5)

print(a.sides)

class Note:

    def __init__(self,title,body):
        self.title = title
        self.body = body

class Notebook:
    data = list()
    # data = [1,2,3,4]

    def add(self,note):
        self.data.append(note)

    def show(self):
        for note in self.data:
            print(note.title)

first = Note('One','1111111')
second = Note('Two','2222222')
color = Notebook()
color.add(first)
color.add(second)
color.show()

with open('numbers1.txt', 'rt') as f:
    a = f.readlines()

for string in a:
    print(string[:-1])

# if __name__ == '__main__':
#     with open('numbers1.txt', 'rt') as f:
#         a = f.readlines()
#
#     for string in a:
#         print(string[:-1])
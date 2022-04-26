'''Задание 4
Создайте класс «Дробь». Необходимо хранить в полях
класса: числитель и знаменатель. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса. Также создайте
методы класса для выполнения арифметических операций
(сложение, вычитание, умножение, деление, и т.д.).'''


class Fraction:
    numerator = int()
    denominator = int()

    def __init__(self, number):  # '11/24'
        self.numerator = int(number[:number.find('/')])
        self.denominator = int(number[number.find('/') + 1:])

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        n1 = self.numerator * other.denominator
        n2 = self.denominator * other.denominator
        n3 = other.numerator * self.denominator
        n4 = other.denominator * self.denominator
        denominator = n2
        numerator = n1 + n3
        return f'{numerator}/{denominator}'

    def decimation(self):
        return self.numerator/self.denominator

#*,-,/ всё для вас

d = Fraction('11/24')
e = Fraction('5/11')
print(d)
print(e)
print(d, '+', e, '=', d + e)

h = Fraction(d+e)
print(h)
print(h.decimation())
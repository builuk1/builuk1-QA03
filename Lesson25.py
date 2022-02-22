# '''Напишите функцию, определяющую количество
# простых чисел в списке целых.
# Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.'''
#
#
# def simple(number):
#     for some_number in range(2, number):
#         if number % some_number == 0:
#             return False
#     return True
#
#
# def simple_list(list_of_numbers):
#     new_list = []
#     for number in list_of_numbers:
#         if simple(number):
#             new_list.append(number)
#     l = len(new_list)
#     return l
#
#
# random_list = [1, 4, 5, 7, 3, 5, 6, 8, 137, 42, 65]
# print(simple_list(random_list))
#
# '''калькулятор'''
# example = '-23-12'
# e_list = []
# if example[0] == '-':
#     if '+' in example[1:]:
#         e_list = example[1:].split('+')
#         e_list.insert(1, '+')
#     elif '-' in example[1:]:
#         e_list = example[1:].split('-')
#         e_list.insert(1, '-')
#     elif '*' in example[1:]:
#         e_list = example[1:].split('*')
#         e_list.insert(1, '*')
#     elif '/' in example[1:]:
#         e_list = example[1:].split('/')
#         e_list.insert(1, '/')
#     e_list[0] = int(e_list[0])
#     e_list[2] = int(e_list[2])
#     e_list[0] = e_list[0] * (-1)
# else:
#     if '+' in example:
#         e_list = example.split('+')
#         e_list.insert(1, '+')
#     elif '-' in example:
#         e_list = example.split('-')
#         e_list.insert(1, '-')
#     elif '*' in example:
#         e_list = example.split('*')
#         e_list.insert(1, '*')
#     elif '/' in example:
#         e_list = example.split('/')
#         e_list.insert(1, '/')
#     e_list[0] = int(e_list[0])
#     e_list[2] = int(e_list[2])
#
# d = {'+': e_list[0] + e_list[2], '-': e_list[0] - e_list[2], '*': e_list[0] * e_list[2], '/': e_list[0] / e_list[2]}
# result = d[e_list[1]]
# print(result)
#
# '''калькулятор by Юрий'''
# s = '-23+12'
# number1 = ''
# number2 = ''
# symb = ['+', '-', '*', '/']
#
# for i in range(len(s)):
#     n = s[i]
#     for j in symb:
#         if n == j:
#             number1 = s[:i]
#             number2 = s[i + 1:]
#             mark = n
# if mark == '+':
#     print(number1, '+', number2, '=', int(number1) + int(number2))
# elif mark == '-':
#     print(number1, '-', number2, '=', int(number1) - int(number2))
# elif mark == '*':
#     print(number1, '*', number2, '=', int(number1) * int(number2))
# elif mark == '/':
#     print(number1, '/', number2, '=', int(number1) / int(number2))
#
# # ООП
# a = int(5)
# b = str('Hello')
# c = list([1, 2, 3])
# print(c.append(2))
#
#
# # 2 + 2 = 5
#
# class Box:
#     v = 5  # аргумент класса, атрибут класса, поле класс, field, переменная класса
#
#     # параметры класса : что? сколько? какой? где? существительное
#     def open(self, count):  # метод класса, method, функция класса
#         print(f'Open {count} box')  # глагол : что сделать? как сделать?
#
#
# lanch = Box()
# print(lanch.v)
# lanch.open(2)
#
# tools = Box()
# tools.open(5)


class Borsch:
    volume = 3
    color = 'red'
    components = ['Beetroot', 'Tomato', 'Meat', 'Potato']
    temperature = 20.5
    vegeterian = False
    create_date = '22/02/2022'
    life_period = 480

    def heating(self):
        self.temperature = self.temperature + 5

    def show_heating(self):
        return self.temperature

    def more_borsch(self):
        self.volume = self.volume + 1

    def show_volume(self):
        return self.volume

    def change_color(self,new_color):
        self.color = new_color


andrii_borsch = Borsch()
print(andrii_borsch.show_heating())
andrii_borsch.heating()
andrii_borsch.heating()
print(andrii_borsch.show_heating())
print(andrii_borsch.show_volume())
andrii_borsch.more_borsch()
andrii_borsch.more_borsch()
print(andrii_borsch.show_volume())

sten_borsch = Borsch()
sten_borsch.color = 'green'
# self.color = new_color

print(andrii_borsch.color)
print(sten_borsch.color)
andrii_borsch.change_color('yellow')
print(andrii_borsch.color)
print(sten_borsch.color)
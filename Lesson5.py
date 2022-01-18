# # AND, OR, NOT
# # Дано 3 переменные, вывести 3 если все они равны, 2 если равны 2 из них и 0 если не равны.
# # a = 2
# # b = 3
# # c = 4
# # if a == b == c:
# #     print(3)
# # elif a == b:
# #     print(2)
# # elif b == c:
# #     print(2)
# # elif a == c:
# #     print(2)
# # else:
# #     print(0)
# #
# # a = 12
# # b = 6
# # c = 4
# # if a >= b >= c:
# #     print(a)
# #     if b >= c:
# #         print(b)
# #         print(c)
# #     else:
# #         print(c)
# #         print(b)
# # elif b >= a >= c:
# #     print(a)
# #     if b >= c:
# #         print(b)
# #         print(c)
# #     else:
# #         print(c)
# #         print(b)
#
# # x = 4
# # y = 0
# # if x > 0:
# #     if y > 0:
# #         print('I')
# #     elif y < 0:
# #         print('IV')
# #     elif y == 0:
# #         print('On Axis X+')
# # elif x < 0:
# #     if y > 0:
# #         print('II')
# #     elif y < 0:
# #         print('III')
# #     elif y == 0:
# #         print('On Axis X-')
# # elif x == 0:
# #     if y > 0:
# #         print('On Axis Y+')
# #     elif y < 0:
# #         print('On Axis Y-')
# #     elif y == 0:
# #         print('ZERO')
#
# # AND
# # True and True  >> True
# # True and False  >> False
# # False and True  >> False
# # False and False  >> False
# # a and b and c
# #
# # #OR
# # True or True  >> True
# # True or False  >> True
# # False or True  >> True
# # False or False  >> False
# # a or b or c
# #
# # (a and b ) or (c and d) or (e and f)
#
# # and запинается на лжи   a and b and c and d and e
# # or запинается на правде a or b or c or d or e
# a = 2
# b = 3
# c = 4
# if a == b and b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)
#
# # Рассмотрим альтернативу if при работе с dict
# x = 0
# y = 0
# if x > 0 and y > 0:
#     print('I')
# elif x > 0 and y < 0:
#     print('IV')
# elif x < 0 and y < 0:
#     print('III')
# elif x < 0 and y > 0:
#     print('II')
# # elif x != 0 and y == 0:
# #     print('On Axis X')
# elif x > 0 and y == 0:
#     print('On Axis X+')
# elif x < 0 and y == 0:
#     print('On Axis X-')
# # elif x == 0 and y != 0:
# #     print('On Axis Y')
# elif y > 0 and x == 0:
#     print('On Axis Y+')
# elif y < 0 and x == 0:
#     print('On Axis Y-')
# elif y == 0 and x == 0:
#     print('ZERO')
a = '''Задание 1
Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность. Если число
четное требуется вывести на экран число и надпись Even
number. Если число нечетное выведите на экран число и
надпись Odd number. '''
print(a)
number = int(input("Enter number : "))
if number == 0:
    print('Zero')
elif number % 2 == 0:
    print('Even')
elif number % 2 != 0:
    print('Odd')
else:
    print('Some error')

a = '''Задание 2
Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. Если число кратно
требуется вывести на экран число и надпись Number is
multiple 7. Если число не кратно выведите на экран число
и надпись Number is not multiple 7.'''
num = int(input("Enter number: "))
if num == 0:
    print("Zero")
elif num % 7 == 0:
    print("Number is multiple 7")
elif num % 7 != 0:
    print("Number is not multiple 7")
else:
    print("Error")

a = 5
b = 4
c = 3
d = 2
e = 1
# if a >= b:
#     if b >= c:
#         if c >= d:
#             if d >= e:
#                 ....
# if a >= b and a >= c and a >= d and a >= e:
# ...
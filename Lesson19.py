# def simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# l = [1, 2, 3]
# print(l.pop())
# print(l.append(4))
#
#
# def pop(somelist):
#     return somelist.pop()
#
#
# def append(somelist, data):
#     somelist.append(data)
#
#
# l = [1, 2, 3]
# print(pop(l))
# print(append(l, 4))
# print(l)
#
#
# # Рекурсия
#
# # return > break
# def somfunction():
#     return 'Something'
#     print("You can't see this in console")
#
#
# while False:
#     print("You can't see this in console")
# if False:
#     print("You can't see this in console")
#
#
# def calc(a, b):  # Позиционные аргументы
#     return a + b
#
#
# print(calc(2, 2))
#
#
# def calc1(a, b, c=2):  # Аргументы по умолчанию
#     return a + b + c
#
#
# print(calc1(2,2))
#range(start,finish,step)
# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         if start < finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     start = start + 1
#         elif start > finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     return numbers
#     else:
#         n = 0
#         while n < start:
#             numbers.append(n)
#             n = n + 1
#     return numbers
#
# for i in range(1,12,1):
#     print(i,end=' ')
# print()
# for i in custom_range(1,12,1):
#     print(i, end=' ')
#
# '''Задание 7
# Напишите функцию, которая проверяет является
# ли шестизначное число «счастливым». Число передаётся в качестве параметра. Если число счастливое нужно
# вернуть из функции true, иначе false.
# «Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых
# цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0,
# а 723422 – несчастливое 7+2+3 != 4+2+2.
# *Любая длинна числа
# 1234|5678  1234|5|7890'''
#
# def lucky(abcdef):
#     abcdef = int(abcdef)
#     n1 = abcdef//100000
#     n2 = (abcdef//10000)%10
#     n3 = (abcdef//1000)%10
#     n4 = (abcdef // 100) % 10
#     n5 = (abcdef // 10) % 10
#     n6 = (abcdef // 1) % 10
#     if n1+n2+n3 == n4+n5+n6:
#         return True
#     else:
#         return False
# print(lucky(124421))
#
# def lucky_number(number):
#     number = str(number)
#     if number[0] + number[1] + number[2] == number[3] + number[4] + number[5]:
#         print('lucky')
#         return True
#     else:
#         print("Not lucky")
#         return False
# print(lucky_number('111111'))
#
# def Lucky(n):
#     n1= (n)//100000
#     n2 = ((n)//10000)%10
#     n3 = ((n)//1000)%10
#     n4 = ((n)//100)%10
#     n5 = ((n)//10)%10
#     n6 = ((n)//1)%10
#     for i in range(n):
#         if n1+n2+n3 == n4+n5+n6:
#             return True
#         else:
#             return False
# n = int(input("Enter your num: "))
# print(Lucky(n))
#
# def lucky_num(a):#str
#     a = str(a)
#     if a.isnumeric():
#         a = int(a)
#         n1 = (a) // 100000
#         n2 = ((a) // 10000) % 10
#         n3 = ((a) // 1000) % 10
#         n4 = ((a) // 100) % 10
#         n5 = ((a) // 10) % 10
#         n6 = ((a) // 1) % 10
#         if n1 + n2 + n3 == n4 + n5 + n6:
#             print("Your number is lucky!")
#             return True
#         else:
#             print("Your number is unlucky!")
#             return False
#     else:
#         print("Error")
#
# print(lucky_num('123456'))
#
# def numbers(number):
#     n1 = (number)//100000
#     n2 = ((number)//10000)%10
#     n3 = ((number)//1000)%10
#     n4 = ((number)//100)%10
#     n5 = ((number)//10)%10
#     n6 = ((number)//1)%10
#     if n1 + n2 + n3 == n4 + n5 + n6:
#         print('Lucky')
#     else:
#         print('Not lucky')
#
# def lucky_num(n):
#     n = str(n)
#     n1 = int(n[0])
#     n2 = int(n[1])
#     n3 = int(n[2])
#     n4 = int(n[3])
#     n5 = int(n[4])
#     n6 = int(n[5])
#     if n1 + n2 + n3 == n4 + n5 + n6:
#         print('Lucky!')
#         return True
#     else:
#         print("Your number is unlucky!")
#         return False
# lucky_num(1213456)
#
# def numbers(number):
#     number = str(number)
#     if number.isnumeric():
#         number = int(number)
#         n1 = (number)//100000
#         n2 = ((number)//10000)%10
#         n3 = ((number)//1000)%10
#         n4 = ((number)//100)%10
#         n5 = ((number)//10)%10
#         n6 = ((number)//1)%10
#         if n1 + n2 + n3 == n4 + n5 + n6:
#             print('Lucky')
#             return True
#         else:
#             print('Not lucky')
#             return False
#     else:
#         print('Error')
#
#
# numbers(123322)
# def calc(a, b):  # Позиционные аргументы
#     return a + b
# print(calc(2, 2))
# def calc1(a, b, c=2):  # Аргументы по умолчанию
#     return a + b + c
# print(calc1(2,2))
# def calc2(a, b, c=2,*args):  # Неопределённое количество позиционных аргументов
#     return a + b + c

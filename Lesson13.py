# #str методы строк
# #итерируемый тип данных\ не изменяемый тип данных\ индексируемый
# h = 'Hello World!'
# #    0123456789
# print(h)
# print(h[0])
# h = h + '?'
# print(h)
# print(h[0])
# print(h[1])
# print(h[2])
# print(h[3])
#
# n = 'Andrii Builuk'
# print(n[0],n[1],n[2])#A n d
# print(n[7],n[8],n[9],n[10],n[2])#B u i l d
# print(n[2],n[3],n[4],n[1],n[12])#d r i n k
#
# '''Задание 1
# Пользователь вводит с клавиатуры строку.
# Произведите поворот строк и полученный результат выведите
# на экран.'''
# s = 'Hello World!'
# # print(len(s))
# # for i in range(len(s)):
# #     print(s[i])
# #V1
# rs = ''
# for i in range(len(s)):
#     rs = s[i] + rs
# print(rs)
#
# #V2
# # h = 'Hello World!'
# #      0123456789
# #  -      987654321
# s = 'Hello World!'
# for i in range(1,len(s)+1):
#     print(s[-i])
# '''Задание 2
# Пользователь вводит с клавиатуры строку. Посчитайте количество букв,
# цифр в строке. Выведите оба
# количества на экран.'''
# #V1
# letters = 'abcdefghijklmnopqrstuvwxyz'
# numbers = '0123456789'
# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letters = count_letters + 1
#     for n in range(len(numbers)):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1
# print(count_numbers,count_letters)
#
# number = '9'
# print(number.isnumeric())
# print(number.isalpha())
# #GDPR
#
# #V2
# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     if a.isalpha():
#         count_letters = count_letters + 1
#     if a.isnumeric():
#         count_numbers = count_numbers + 1
# print(count_numbers,count_letters)

'''Задание 3
Пользователь вводит с клавиатуры строку и символ
для поиска. Посчитайте сколько раз в строке встречается
искомый символ. Полученное число выведите на экран.'''
# s = 'Abrakadabra'
# symbol = 'a'
# count = 0
# for i in range(len(s)):
#     if s[i] == symbol:
#         count = count + 1
# print(count)
#
# print(s.count(symbol))

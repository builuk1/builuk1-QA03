# a = 1
# b = 10
# while a <= b and a != 5:
#     print(a)
#     a = a + 1
#
# a = 1
# b = 10
# for i in range(a,b+1):
#     if i == 5:
#         break
#     print(i)

# a = 1
# b = 10
# while True:
#     print(a)
#     a = a + 1
#     if a == 5:
#         break

# a = 1
# b = 10
# for i in range(a,b+1):
#     if i == 5:
#         print('GO')
#         continue
#     print(i)

# a = 1
# b = 7
# guess = 4
# if a <= guess and guess <= b:
#     for i in range(a,b + 1):
#         if i == guess:
#             print('!',i,'!',sep='', end = ' ')
#         else:
#             print(i, end = ' ')


'''Задание 1
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран заполненный
квадрат. Размер стороны равен введённому размеру.
Например, если пользователь ввёл 3 на экране будет
выведено:
***
***
***
Задание 2
Пользователь вводит с клавиатуры ширину и высоту прямоугольника. Требуется отобразить на экран
заполненный прямоугольник с указанными высотой и
шириной. Например, если пользователь ввёл высоту 3,
а ширину 5 на экране будет выведено:
*****
*****
*****'''
# width = 3
# height = 3
# symbol = '*'
# for i in range(height):
#     print(width * symbol)

# a=3
# for i in range(1,a+1):
#     print('%'*a)

'''
Задание 3
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран незаполненный квадрат 
(отображаются только границы квадрата).
Размер стороны равен введённому размеру.

'''

width = 5
height = 5
symbol = '*'
space = ' '
for i in range(height):
    if i == 0 or i == (height - 1):
        print(width * symbol)
    else:
        print(symbol + ((width - 2) * space) + symbol)

import random
width = 3
height = 3
for i in range(height):
    for j in range(width):
        sym = random.randint(1, 9)
        print(f"{sym}",end=' ')
    print()
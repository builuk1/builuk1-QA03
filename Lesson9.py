# a = 0
# while a < 10:
#     print(a)
#     a = a + 1
#
# for i in 0,1,2,3,4,5,6,7,8,9:
#     print(i)
#
# for student in 'Andrey', 'Sten', 'Ben', 'Glen':
#     print(student)
#
# for i in 0, 2, 4, 6, 8, 10:
#     print(i)
#
# for i in 'Hello World':
#     print(i, end=' ')
# print()
#
# for i in range(0, 10):
#     print(i)

'''Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
показать все числа в указанном диапазоне.'''
# a = 0
# b = 10
# for i in range(a, b + 1):  #(0,до,1),(от,до,1),(от,до,шаг)
#     print(i)

'''Задание 2
Пользователь вводит с клавиатуры два числа. Нужно
показать все нечетные числа в указанном диапазоне.
Задание 3
Пользователь вводит с клавиатуры два числа. Нужно
показать все четные числа в указанном диапазоне.'''
# a = 5
# b = 15
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i)
#
# a = 5
# b = 15
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(i)

'''Задание 4
Пользователь вводит с клавиатуры два числа. 
Нужно показать все числа в указанном диапазоне в порядке
убывания.'''
# num1 = 1
# num2 = 10
# for i in range(num2, num1, -1):
#     print(i)
#
#
# num1 = 1
# num2 = 10
# for i in range(num1, num2 + 1):
#     print((i-num2-1) * (-1))

'''Задание 5
Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные 
числа в указанном диапазоне.
Если границы диапазона указаны неправильно требуется
произвести нормализацию границ. Например, пользователь ввел 33 и 13, 
требуется нормализация после которой
начало диапазона станет равно 13, а конец 33.'''

num1 = 33
num2 = 13
if num1 > num2:
    for i in range(num2, num1 + 1):
        if i % 2 != 0:
            print(i)
else:
    for i in range(num1, num2 + 1 ):
        if i % 2 != 0:
            print(i)

'''Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
посчитать сумму чисел в указанном диапазоне, а также
среднеарифметическое.
Задание 2
Пользователь вводит с клавиатуры число. Требуется
посчитать факториал числа. Например, если введено 3,
факториал числа 1*2*3 = 6.
Формула для расчета факториала: n! = 1*2*3…*n, где
n — число для расчета факториала'''

sum = 0
av = 0
count = 0
mult = 1
a = 1
b = 6
for i in range(a,b + 1):
    sum = sum + i# 1
    count = count + 1# 1
    mult = mult * i # 2
av = sum / count
print(f'First sum : {sum}, av : {av}\nSecond mult : {mult}')

a = 1
b = 6
count = 0
aver = 0
sum = 0
for i in range(a, b + 1):
    count = count + 1
    sum = count + i#ошибка
aver = sum / count
print(f"Sum = {sum}\nAverage = {aver}")

'''Задание 3
Пользователь вводит с клавиатуры длину линии.
Нужно отобразить на экране горизонтальную линию
из *, указанной длины.
Например, если было введено 7, тогда вывод на экран
будет такой: *******.
Задание 4
Пользователь вводит с клавиатуры длину линии и
символ для заполнения линии. Нужно отобразить на
экране горизонтальную линию из введенного символа,
указанной длины.
Например, если было введено 5 и &, тогда вывод на
экран будет такой: &&&&&.'''
length = 10
symbol = '&'
for i in range(length):
    print(symbol, end= ' ')
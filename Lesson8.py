# '''Задание 3
# Пользователь вводит с клавиатуры длину линии.
# Нужно отобразить на экране горизонтальную линию
# из *, указанной длины.
# Например, если было введено 7, тогда вывод на экран
# будет такой: *******.'''
# a = 10
# while a > 0:
#     print("*",end='')
#     a = a - 1
# print()
# a = 10
# s = ''
# while a > 0:
#     s = s + '*'
#     a = a - 1
# print(s)
# '''Задание 4
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране горизонтальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и &, тогда вывод на
# экран будет такой: &&&&&.'''
# a = 10
# s = ''
# l = '&'
# while a > 0:
#     s = s + l
#     a = a - 1
# print(s)

#Guess my number
# import random
# secret_number = random.randint(1,20)
# guess_number = 0
# while secret_number != guess_number:
#     guess_number = int(input("Enter number : "))
#     if secret_number < guess_number:
#         print('Your number greater than secret\nТвоё число больше, чем загаданное')
#     elif secret_number > guess_number:
#         print('Your number less than secret\nТвоё число меньше, чем загаданное')
# print('YOU WIN!!!')
# import random
# secret_number = random.randint(1,20)
# guess_number = 0
# lifes = 5
# while secret_number != guess_number and lifes > 0:
#     guess_number = int(input("Enter number : "))
#     lifes = lifes - 1
#     print(f'You have {lifes} lifes')
#     if secret_number < guess_number:
#         print('Your number greater than secret\nТвоё число больше, чем загаданное')
#     elif secret_number > guess_number:
#         print('Your number less than secret\nТвоё число меньше, чем загаданное')
# if lifes > 0:
#     print('YOU WIN!!!')
# else:
#     print('YOU LOSE')

#pet project
# import random
# game = True
# money = 0
# while game:
#     secret_number = random.randint(1,20)
#     guess_number = 0
#     lifes = 5
#     while secret_number != guess_number and lifes > 0:
#         guess_number = int(input("Enter number : "))
#         lifes = lifes - 1
#         print(f'You have {lifes} lifes')
#         if secret_number < guess_number:
#             print('Your number greater than secret\nТвоё число больше, чем загаданное')
#         elif secret_number > guess_number:
#             print('Your number less than secret\nТвоё число меньше, чем загаданное')
#     if lifes > 0:
#         print('YOU WIN!!!')
#         money = money + 5
#     else:
#         print('YOU LOSE')
#     print(f'You have {money} money')

# work = True
# while work:
#     number1 = 2#int(input("Enter number1 : "))
#     command = '+'#str(input("Enter operation : "))
#     number2 = 2#int(input("Enter number2 : "))
#     if command == '+':
#         print(f'{number1} {command} {number2} = {number1 + number2}')
#     # while command == '+':
#     #     print(f'{number1} {command} {number2} = {number1 + number2}')
#     #     command = ''
#     elif command == '-':
#         print(f'{number1} {command} {number2} = {number1 - number2}')
#     elif command == '*':
#         print(f'{number1} {command} {number2} = {number1 * number2}')
#     elif command == '/':
#         print(f'{number1} {command} {number2} = {number1 / number2}')
#     work = str(input("Press any key to continue : "))

'''Задание 1
Показать таблицу умножения для числа, введенного
пользователем. Например, если пользователь вводит
число 7, нужно показать:
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21'''
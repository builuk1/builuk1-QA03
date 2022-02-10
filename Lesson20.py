# # def calc(a, b):  # Позиционные аргументы
# #     return a + b
# # print(calc(2, 2))
# # def calc1(a, b, c=2):  # Аргументы по умолчанию
# #     return a + b + c
# # print(calc1(2,2))
# # def calc2(a, b, c=2,*args):  # Неопределённое количество позиционных аргументов
# #     return a + b + c
# # def average(*numbers):  # название переменной аргумента, может быть любой
# #     # *numbers это кортеж
# #     count = len(numbers)
# #     sum = 0
# #     for number in numbers:
# #         sum = sum + number
# #     return sum / count
# #
# #
# # print(average(1, 2, 5, 4, 3))
# #
# #
# # # def calc2(a, b, c=2,*args,**kwargs):  # Аргументы с ключевыми словами
# # #     return a + b + c
# # # calc2(2,3,1,1,2,3,4,2,3,4,2,f='3',g='')
# # def create_note(**notes):
# #     # **notes словарь
# #     return notes
# #
# #
# # print(create_note(andrey='teacher', sten='builder', glen='sailor'))
#
# # LEGB
# # Области видимости функции
# # Local Enclosed Global BuiltIn
#
# # Local
# # import random
# #
# # a = 1
# # b = 11
# # def some():
# #     a = 2#это другая а, которая существует только внутри функции
# #     # b = 1
# #     # b = b + 2
# #     a = a * a
# #     print(a)
# #     print(b)
# #     print('Finish')
# #
# # print(a)
# # some()
# #
# # c = 2
# # def local_some():
# #     global c#не безопасно
# #     c = c + 3
# #
# # local_some()
# # print(c)
# # local_some()
# # print(c)
# # local_some()
# # print(c)
# # local_some()
# # print(c)
# #
# # #Enclosed
# # a = 2 #В ГЛОБАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ
# # def first():
# #     global a
# #     b = 3 #В ЛОКАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ ПО ОТНОШЕНИЮ К a
# #             # В ЕНКЛОСЕД ОБЛАСТИ ВИДИМОСТИ ПО ОТНОШЕНИЮ К с
# #     def second():
# #         global a
# #         #global b неправильно
# #         nonlocal b
# #         c = 4#В ЛОКАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ ПО ОТНОШЕНИЮ К a
# # #Global вся ваша программа в текущем файле
# # #BuiltIn область видимости интерпретатора len() del() list() str()
# #
# # '''Задание 4
# # Написать игру «Крестики-нолики».'''
# # #Крестики Нолики
# # #Tic Tac Toe
# # #Variables
# # count = 0
# # player1_symbol = 'X'
# # player2_symbol = 'O'
# # player1_choice = '0'
# # player2_choice = '0'
# # board = [0,'1','2','3','4','5','6','7','8','9']
# # board = f'{board[1]}|{board[2]}|{board[3]}\n-----\n{board[4]}|{board[5]}|{board[6]}\n-----\n{board[7]}|{board[8]}|{board[9]}'
# # turn = 'X'
# # winner = ''
# # def show_board(board):
# #     return board
# # def player_choice():
# #     while True:
# #         #Game choice
# #         player1_choice = str(input(f'Enter your choice {player1_symbol}: '))
# #         #Board update
# #         if board[int(player1_choice)] == player1_choice:
# #             board[int(player1_choice)] = 'X'
# #             break
# # def check_winner():
# #     if board[1] == board[2] == board[3]:
# #         if board[1] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[1] == player2_symbol:
# #             winner = 'O'
# #             return winner
# #     if board[4] == board[5] == board[6]:
# #         if board[4] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[4] == player2_symbol:
# #             winner = 'O'
# #             return winner
# #     if board[7] == board[8] == board[9]:
# #         if board[7] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[7] == player2_symbol:
# #             winner = 'O'
# #             return winner
# #     if board[1] == board[4] == board[7]:
# #         if board[1] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[1] == player2_symbol:
# #             winner = 'O'
# #             return winner
# #     if board[2] == board[5] == board[8]:
# #         if board[2] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[2] == player2_symbol:
# #             winner = 'O'
# #             return winner
# #     if board[3] == board[6] == board[9]:
# #         if board[3] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[3] == player2_symbol:
# #             winner = 'O'
# #             return winner
# #     if board[7] == board[5] == board[3]:
# #         if board[7] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[7] == player2_symbol:
# #             winner = 'O'
# #             return winner
# #     if board[1] == board[5] == board[9]:
# #         if board[1] == player1_symbol:
# #             winner = 'X'
# #             return winner
# #         elif board[1] == player2_symbol:
# #             winner = 'O'
# #             return winner
# # def bot_choice():
# #     while True:
# #         #Game choice
# #         player2_choice = random.randint(1,9)
# #         if board[int(player2_choice)] == player2_choice:
# #             board[int(player2_choice)] = 'O'
# #             break
# #
# # while count <= 9:
# #     show_board(board)
# #     player_choice()
# #     count = count + 1
# #     if check_winner() != '':
# #         break
# #     if count == 9:
# #         break
# #     bot_choice()
# #     count = count + 1
# #
# # if winner == 'X':
# #     print('Player 1 win the game!')
# # elif winner == 'O':
# #     print('Player 2 win the game!')
# # elif winner == '':
# #     print('Draw')
# #
#
# #Рекурсия
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))
# print(factorial(6))
#


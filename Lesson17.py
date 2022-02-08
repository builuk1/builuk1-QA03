l = [1, 2, 3]  # list
t = (1, 2, 3)  # tuple
d = {'a': 1, 'b': 2, 'c': 3}  # dictionary
s = {1, 2, 3, 4, 5}  # set
fs = {1, 2, 3, 4, 5}  # frozenset
#
# for element in l:
#     print(element)
#
# for i in range(len(l)):
#     print(l[i])
#
# a = [i for i in range(10)]  # inline
# print(a)
#
# # without if (dict)
# n1 = 12
# command = '-'
# n2 = 2
# calc = {'+': n1 + n2, '-': n1 - n2}
# print(calc[command])
#
# # Многомерные массивы
# l2 = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9]]
# print(l2)
# for i in range(len(l2)):
#     for j in range(len(l2[i])):
#         print(l2[i][j], end=' ')
#     print()
# print(l2[1][1])
# # pythontutor.ru
# l2 = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9]]
# for i in range(len(l2)):
#     print(l2[i][0], l2[i][1], l2[i][2])
#
# # 2d_array board
# tictactoe_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for y in range(9):
#     turn = int(input("Enter number of cell: "))
#     for i in range(len(tictactoe_board)):
#         for j in range(len(tictactoe_board[i])):
#             if tictactoe_board[i][j] == turn:
#                 tictactoe_board[i][j] = 'X'
#     for i in range(len(tictactoe_board)):
#         for j in range(len(tictactoe_board[i])):
#             print(tictactoe_board[i][j], end=' ')
#         print()
#
# d = {'a': 1, 'b': 2, 'c': 3}  # dictionary
# coord = {(0, 0, 0): 1, (0, 0, 1): 2}
#

s = {1, 2, 3, 4, 5}  # set
fs = {1, 2, 3, 4, 5}  # frozenset  кортеж множество

s = set('abbbcd')
print(s)
#split analog
s = list('abbbcd')
print(s)
s = 'a+b+b+b+c+d'
s = s.split('+')
print(s)
s = set([1,2,3,4,4,4])
print(s)
s = set((1,2,3,3,4,5))
print(s)
s = set({'a': 1, 'b': 2, 'c': 3})
print(s)

some_list = [1,3,4,3,6,4,6,3,9,4,8,0,5,3]
print(some_list.__sizeof__())
some_list = list(set(some_list))
print(some_list.__sizeof__())
print(some_list)
users = [('Andrey',12345),('Sten',12345),('Andrey',12345)]
users = list(set(users))
users = []
users = list()
print(users)


fs = {1, 2, 3, 4, 5}  # frozenset  кортеж множество
fs = frozenset(users)
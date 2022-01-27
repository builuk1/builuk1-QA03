#Крестики Нолики
#Tic Tac Toe
#Variables
count = 0
player1_symbol = 'X'
player2_symbol = 'O'
player1_choice = '0'
player2_choice = '0'
board_1 = '1'
board_2 = '2'
board_3 = '3'
board_4 = '4'
board_5 = '5'
board_6 = '6'
board_7 = '7'
board_8 = '8'
board_9 = '9'
turn = 'X'
winner = ''
#Show board (simple)
# print(board_1,board_2,board_3)
# print(board_4,board_5,board_6)
# print(board_7,board_8,board_9)
while count <= 9:
    #Show board (pro)
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)

    while True:
        #Game choice
        player1_choice = str(input(f'Enter your choice {player1_symbol}: '))
        #Board update
        if player1_choice == board_1:
            board_1 = player1_symbol
            break
        elif player1_choice == board_2:
            board_2 = player1_symbol
            break
        elif player1_choice == board_3:
            board_3 = player1_symbol
            break
        elif player1_choice == board_4:
            board_4 = player1_symbol
            break
        elif player1_choice == board_5:
            board_5 = player1_symbol
            break
        elif player1_choice == board_6:
            board_6 = player1_symbol
            break
        elif player1_choice == board_7:
            board_7 = player1_symbol
            break
        elif player1_choice == board_8:
            board_8 = player1_symbol
            break
        elif player1_choice == board_9:
            board_9 = player1_symbol
            break
    count = count + 1
    #Check winner(simple)
    if board_1 == board_2 == board_3:
        if board_1 == player1_symbol:
            winner = 'X'
            break
        elif board_1 == player2_symbol:
            winner = 'O'
            break
    if board_4 == board_5 == board_6:
        if board_4 == player1_symbol:
            winner = 'X'
            break
        elif board_4 == player2_symbol:
            winner = 'O'
            break
    if board_7 == board_8 == board_9:
        if board_7 == player1_symbol:
            winner = 'X'
            break
        elif board_7 == player2_symbol:
            winner = 'O'
            break
    if board_1 == board_4 == board_7:
        if board_1 == player1_symbol:
            winner = 'X'
            break
        elif board_1 == player2_symbol:
            winner = 'O'
            break
    if board_2 == board_5 == board_8:
        if board_2 == player1_symbol:
            winner = 'X'
            break
        elif board_2 == player2_symbol:
            winner = 'O'
            break
    if board_3 == board_6 == board_9:
        if board_3 == player1_symbol:
            winner = 'X'
            break
        elif board_3 == player2_symbol:
            winner = 'O'
            break
    if board_7 == board_5 == board_3:
        if board_7 == player1_symbol:
            winner = 'X'
            break
        elif board_7 == player2_symbol:
            winner = 'O'
            break
    if board_1 == board_5 == board_9:
        if board_1 == player1_symbol:
            winner = 'X'
            break
        elif board_1 == player2_symbol:
            winner = 'O'
            break
    #Show board (pro)
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)

    if count == 9:
        break
    while True:
        #Game choice
        player2_choice = str(input(f'Enter your choice {player2_symbol}: '))
        #Board update
        if player2_choice == board_1:
            board_1 = player2_symbol
            break
        elif player2_choice == board_2:
            board_2 = player2_symbol
            break
        elif player2_choice == board_3:
            board_3 = player2_symbol
            break
        elif player2_choice == board_4:
            board_4 = player2_symbol
            break
        elif player2_choice == board_5:
            board_5 = player2_symbol
            break
        elif player2_choice == board_6:
            board_6 = player2_symbol
            break
        elif player2_choice == board_7:
            board_7 = player2_symbol
            break
        elif player2_choice == board_8:
            board_8 = player2_symbol
            break
        elif player2_choice == board_9:
            board_9 = player2_symbol
            break
    count = count + 1
    #Check winner(simple)
    if board_1 == board_2 == board_3:
        if board_1 == player1_symbol:
            winner = 'X'
            break
        elif board_1 == player2_symbol:
            winner = 'O'
            break
    if board_4 == board_5 == board_6:
        if board_4 == player1_symbol:
            winner = 'X'
            break
        elif board_4 == player2_symbol:
            winner = 'O'
            break
    if board_7 == board_8 == board_9:
        if board_7 == player1_symbol:
            winner = 'X'
            break
        elif board_7 == player2_symbol:
            winner = 'O'
            break
    if board_1 == board_4 == board_7:
        if board_1 == player1_symbol:
            winner = 'X'
            break
        elif board_1 == player2_symbol:
            winner = 'O'
            break
    if board_2 == board_5 == board_8:
        if board_2 == player1_symbol:
            winner = 'X'
            break
        elif board_2 == player2_symbol:
            winner = 'O'
            break
    if board_3 == board_6 == board_9:
        if board_3 == player1_symbol:
            winner = 'X'
            break
        elif board_3 == player2_symbol:
            winner = 'O'
            break
    if board_7 == board_5 == board_3:
        if board_7 == player1_symbol:
            winner = 'X'
            break
        elif board_7 == player2_symbol:
            winner = 'O'
            break
    if board_1 == board_5 == board_9:
        if board_1 == player1_symbol:
            winner = 'X'
            break
        elif board_1 == player2_symbol:
            winner = 'O'
            break

if winner == 'X':
    print('Player 1 win the game!')
elif winner == 'O':
    print('Player 2 win the game!')
elif winner == '':
    print('Draw')
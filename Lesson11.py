#Камень Ножницы Бумага
#Rock Paper Scissors

#Variables
player1_score = 0
player2_score = 0
player1_choice = ''
player2_choice = ''
rounds = 3

#Start of game
for i in range(1,rounds+1):
    #Enter data
    player1_choice = str(input("Enter your choice player 1: [r],[p],[s] : "))#r
    player2_choice = str(input("Enter your choice player 2: [r],[p],[s] : "))#p
    #Compare data

    # if player1_choice == 'r':
    #     if player2_choice == 's':
    #         print('Player 1 win the round!')
    #         player1_score = player1_score + 1
    #     elif player2_choice == 'p':
    #         print('Player 2 win the round!')
    #         player2_score = player2_score + 1
    #     else:
    #         print('Draw round')
    if player1_choice == player2_choice:
        print('Draw round')
    elif player1_choice == 'r':
        if player2_choice == 's':
            print('Player 1 win the round!')
            player1_score = player1_score + 1
        else:
            print('Player 2 win the round!')
            player2_score = player2_score + 1
    elif player1_choice == 'p':
        if player2_choice == 'r':
            print('Player 1 win the round!')
            player1_score = player1_score + 1
        else:
            print('Player 2 win the round!')
            player2_score = player2_score + 1
    elif player1_choice == 's':
        if player2_choice == 'p':
            print('Player 1 win the round!')
            player1_score = player1_score + 1
        else:
            print('Player 2 win the round!')
            player2_score = player2_score + 1
#Compare score
if player1_score > player2_score:
    print('Player 1 win the game!')
elif player2_score > player1_score:
    print('Player 2 win the game!')
else:
    print('Draw game!')

#Камень Ножницы Бумага
#Rock Paper Scissors
game = True
global_player1_score = 0
global_player2_score = 0
while game:
    #Variables
    player1_choice = ''
    player2_choice = ''
    player1_score = 0
    player2_score = 0
    rounds = 3

    #Start of game
    for i in range(1,rounds+1):
        player1_choice = ''
        player2_choice = ''
        #Enter data
        while player1_choice != 'r' and  player1_choice != 'p' and player1_choice != 's':
            player1_choice = str(input("Enter your choice player 1: [r],[p],[s] : "))
        while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 's':
            player2_choice = str(input("Enter your choice player 2: [r],[p],[s] : "))
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
        global_player1_score = global_player1_score + 1
    elif player2_score > player1_score:
        print('Player 2 win the game!')
        global_player2_score = global_player2_score + 1
    else:
        print('Draw game!')
    game = bool(input("If you want continue press any key : "))
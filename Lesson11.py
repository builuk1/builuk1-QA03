#Камень Ножницы Бумага
#Rock Paper Scissors
import random
game = True
global_player1_score = 0
global_player2_score = 0
game_type = 'pvp'#pve
while game:
    #Variables
    player1_choice = ''
    player2_choice = ''
    player1_score = 0
    player2_score = 0
    player1_name = str(input("Enter your name player 1 : "))
    player2_name = 'Unknown'
    if game_type == 'pvp':
        player2_name = str(input("Enter your name player 2 : "))
    elif game_type == 'pve':
        player2_name = 'Bot'
    rounds = 3

    #Start of game
    for i in range(1,rounds+1):
        player1_choice = ''
        player2_choice = ''
        #Enter data
        while player1_choice != 'r' and  player1_choice != 'p' and player1_choice != 's':
            player1_choice = str(input(f"Enter your choice {player1_name}: [r],[p],[s] : "))
        while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 's':
            if game_type == 'pvp':
                player2_choice = str(input(f"Enter your choice {player2_name}: [r],[p],[s] : "))
            elif game_type == 'pve':
                player2_name = random.choice('rps')#Выбирает 1 символ l - lizard, k - Spock
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
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'p':
            if player2_choice == 'r':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 's':
            if player2_choice == 'p':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
    #Compare score
    if player1_score > player2_score:
        print(f'{player1_name} win the game!')
        global_player1_score = global_player1_score + 1
    elif player2_score > player1_score:
        print(f'{player2_name} win the game!')
        global_player2_score = global_player2_score + 1
    else:
        print('Draw game!')
    game = bool(input("If you want continue press any key : "))
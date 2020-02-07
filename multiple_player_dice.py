# A DICE GAME THAT YOU CAN ADD ANY NUMBER OF PLAYERS By Anthony Nwobodo

from random import randint
from time import sleep


def play(num_of_players):
    players = int(num_of_players)

    a = [0] * players
    j = 1

    while j < 4:
        for i in range(len(a)):
            print(f'player {i + 1} it is your turn to play')
            x = input('do you want to roll the dice? [Y/N]: ')
            if x == 'y':
                score = randint(1, 6)
                a[i] += score
                print(f'player {i + 1} rolled and got ===> [{score}]')
            else:
                print(f'Player {i + 1} withdrew from from the game')
                sleep(1)
                y = input('\n Enter "play" to restart the game[play]:  ')
                if y == 'play':
                    play(input('Enter Number of Players: '))

        print(f'\n Round {j} is over, next round begins in 3 seconds')
        sleep(3)
        j += 1
    print(' ################## RESULT ##################')
    for v in range(len(a)):
        print(f'Player {v + 1} Has a Total Score of ===> [{a[v]}]')


play(input('Enter Number of Players: '))

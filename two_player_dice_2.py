import random


def roll():
    out = []
    for i in range(2):
        dice_number = random.randrange(1, 6)
        out.append(dice_number)
    return out


def play_round():
    print('Start')
    result = [0, 0]
    out = [0, 0]
    dict_ = {}
    rounds = 3
    num_of_players = 2
    while rounds >= 1:
        select = input('Roll dice? [y]')
        if select == 'y':
            # Dice rolling logic goes here
            for i in range(num_of_players):
                dict_[i] = roll()
                player = dict_.get(i)
                print(f'Player {i+1}: {player[i]} {player[i]+1}')
                result[0] = result[0]+player[i]
                result[1] = result[1]+player[i]+1
                out[i] += (sum(result))
                print(f'Player {i+1}\'s total: {out[i]}')
                result = [0, 0]

            rounds -= 1
    if out[0] > out[1]:
        print(f'Player 1 wins with {out[0]} points')
    elif out[1] > out[0]:
        print(f'Player 2 wins with {out[1]} points')
    else:
        print('There is a tie')
        play_round()

    select = input('Play again? [y/n]')
    while select not in ['y', 'n']:
        select = input('Play again? [y/n]')
    if select == 'y':
        play_round()
    elif select == 'n':
        pass


play_round()

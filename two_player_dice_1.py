
from random import randint
from time import sleep


def play():

    player_one_scores = 0
    player_two_scores = 0

    for i in range(3):
        print("Player 1 it's your turn.")
        userOneInput = input(
            " Do you want to roll [Y/N]: ")
        if userOneInput == "y":

            valueOne = randint(1, 6)
            print("Player 1 rolled ", valueOne)
            print(" Player 2 it's your turn.")
            userTwoInput = input(
                " Do you want to roll [Y/N]: ")
            if userTwoInput == "y":
                valueTwo = randint(1, 6)
                print("Player 2 rolled ",  valueTwo)
                if valueOne > valueTwo:
                    print("Player 1 wins this round! ")
                    player_one_scores += 1
                elif valueOne == valueTwo:
                    print("It's a draw for this round! ")
                else:
                    print("Player 2 wins this round;")
                    player_two_scores += 1
            elif userTwoInput == "n":
                print("Player 1 wins this round! ")
                player_one_scores += 1
            else:
                print("Program ended abruptly")
                break
        elif userOneInput == "n":
            print("Player 2 wins this round! ")
            player_two_scores += 1
        else:
            print("Program ended abruptly. ")
            break

    sleep(2)

    print("\n Final results: ", player_one_scores, "-", player_two_scores)
    if player_one_scores > player_two_scores:
        print("\n Player 1 is the winner! ")
    elif player_one_scores == player_two_scores:
        print("\n It's a draw! ")
        print("Knockout round begins in 2 seconds")
        sleep(2)
        play()
    else:
        print("\n Player 2 is the winner! ")


play()

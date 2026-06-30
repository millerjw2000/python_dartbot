from random import *
from math import *
import sys
import game
import bot

# this file is basically just for testing the backend without having to run the flask app

def main():

    if len(sys.argv) != 2:
        print('invalid amount of arguments')
        return None
    
    try:
        difficulty = int(sys.argv[1])
    except ValueError as e:
        print('invalid usage')
        return None
    
    print('starting game on difficulty',difficulty)

    new_game = game.Game()

    bigbot = bot.Bot(1)

    #print(board)

    while (True):

        for i in range(3):

            entry = input('enter your hit: ')
            new_game.enter_hit(1,entry)

        if new_game.check_for_win():
            print('player 1 wins!')
            break

        print(new_game.player_boards)
        print(new_game.player_scores)

        for i in range(3):

            aim = bigbot.decide_aimpoint(new_game)
            print('bot is aiming at',aim)
            actual_hit = bigbot.determine_hit(aim)
            print('bot hit a',actual_hit)
            new_game.enter_hit(2,actual_hit)

        if new_game.check_for_win():
            print('player 2 wins!')
            break

        print(new_game.player_boards)
        print(new_game.player_scores)   

if __name__ == '__main__':
    main()
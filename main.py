from random import *
from math import *
import sys
import game
import bot

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

        entry = input('enter your hits: ')

        new_game.enter_hits(entry)

        bot_entry = ''
        for i in range(3):

            aim = bigbot.decide_aimpoint(new_game)
            bot_entry += aim + ' '

        print(bot_entry)

if __name__ == '__main__':
    main()
from math import *
from random import *

difficulty_values = {
    '1' : 60,
    '2' : 40,
    '3' : 25,
}

aimpoints = {
    
    'T20':(0,111),
    'D20':(0,174),
    '20':(0,142),
    
    'T19':(-34,-105),
    'D19':(-53,-165),
    '19':(-43,-135),
    
    'T18':(65,89),
    'D18':(102,140),
    '18':(83,114),
    
    'T17':(34,-105),
    'D17':(53,-165),
    '17':(43,-135),
    
    'T16':(-89,-65),
    'D16':(-140,-102),
    '16':(-114,-83),
    
    'T15':(89,-65),
    'D15':(140,-102),
    '15':(114,-83),
    
    'T14':(-105,34),
    'D14':(-165,53),
    '14':(-135,43),
    
    'T13':(105,34),
    'D13':(165,53),
    '13':(135,43),
    
    'T12':(-65,89),
    'D12':(-102,140),
    '12':(-83,114),
    
    'T11':(-111,0),
    'D11':(-174,0),
    '11':(-142,0),
    
    'T10':(105,-34),
    'D10':(165,-53),
    '10':(135,-43),
    
    'T9':(-89,65),
    'D9':(-140,102),
    '9':(-114,83),
    
    'T8':(-105,-34),
    'D8':(-165,-53),
    '8':(-135,-43),
    
    'T7':(-65,-89),
    'D7':(-102,-140),
    '7':(-83,-114),
    
    'T6':(174,0),
    'D6':(142,0),
    '6':(111,0),
    
    'T5':(-34,105),
    'D5':(-53,165),
    '5':(-43,135),
    
    'T4':(89,65),
    'D4':(140,102),
    '4':(114,83),
    
    'T3':(0,-111),
    'D3':(0,-174),
    '3':(0,-142),
    
    'T2':(65,-89),
    'D2':(102,-140),
    '2':(83,-114),
    
    'T1':(34,105),
    'D1':(53,165),
    '1':(43,135),
    
    'BULL':(0,0),
    'DBULL':(0,0)
             
    }

class Bot:

    def __init__(self,difficulty):
        
        self.difficulty = difficulty

    def decide_aimpoint(self, game: object) -> str:

        #TODO - make it so the bot aims at singles if it just needs a couple points 
        
        game_boards = game.player_boards
        player_scores = game.player_scores

        # if bot is losing, it will try to point
        # if it is winning or tied, it will try to keep closing numbers

        if player_scores[1] < player_scores[0]:

            # check for the highest number it can point on

            for key in game_boards[0]:
                
                if game_boards[1][key][0] >= 3 and game_boards[0][key][0] < 3:

                    if key != 'BULL':
                        return 'T' + key
                    else:
                        return 'DBULL'

            for key in game_boards[0]:
                
                if game_boards[0][key][0] < 3:

                    if key != 'BULL':
                        return 'T' + key
                    else:
                        return 'DBULL'
        
        elif player_scores[1] >= player_scores[0]:      
            
            for key in game_boards[0]:

                if game_boards[1][key][0] < 3:

                    if key != 'BULL':
                        return 'T' + key
                    else:
                        return 'DBULL'
                    
        return 'DBULL'

    def determine_hit(self, aimpoint: str) -> str:

        r = difficulty_values[self.difficulty]

        aimpoint = aimpoints[aimpoint]
        xdist = randint(-r,r)
        ydist = randint(-r,r)
        x = aimpoint[0] + xdist
        y = aimpoint[1] + ydist

        loc = ''
        n = x**2 + y**2
        #print(x,y,n)
        
        if (n > 178**2):
            return '0'
        elif (n > 170**2):
            loc += 'D'
        elif (170**2 > n > 115**2):
            pass
        elif (115**2 > n > 107**2):
            loc += 'T'
        elif (107**2 > n > 16**2):
            pass
        elif (16**2 > n > 6.35**2):
            return 'BULL'
        else:
            return 'DBULL'
        
        if tan(radians(99)) * x - y < 0 and tan(radians(81)) * x - y < 0:
            return loc + '20'
        
        if tan(radians(81)) * x - y > 0 and tan(radians(63)) * x - y < 0:
            return loc + '1'
        
        if tan(radians(63)) * x - y > 0 and tan(radians(45)) * x - y < 0:
            return loc + '18'
        
        if tan(radians(45)) * x - y > 0 and tan(radians(27)) * x - y < 0:
            return loc + '4'
        
        if tan(radians(27)) * x - y > 0 and tan(radians(9)) * x - y < 0:
            return loc + '13'
        
        if tan(radians(9)) * x - y > 0 and tan(radians(171)) * x - y < 0:
            return loc + '6'
        
        if tan(radians(171)) * x - y > 0 and tan(radians(153)) * x - y < 0:
            return loc + '10'
        
        if tan(radians(153)) * x - y > 0 and tan(radians(135)) * x - y < 0:
            return loc + '15'
        
        if tan(radians(135)) * x - y > 0 and tan(radians(117)) * x - y < 0:
            return loc + '2'
        
        if tan(radians(117)) * x - y > 0 and tan(radians(99)) * x - y < 0:
            return loc + '17'
        
        if tan(radians(99)) * x - y > 0 and tan(radians(81)) * x - y > 0:
            return loc + '3'
        
        if tan(radians(81)) * x - y < 0 and tan(radians(63)) * x - y > 0:
            return loc + '19'
        
        if tan(radians(63)) * x - y < 0 and tan(radians(45)) * x - y > 0:
            return loc + '7'
        
        if tan(radians(45)) * x - y < 0 and tan(radians(27)) * x - y > 0:
            return loc + '16'
        
        if tan(radians(27)) * x - y < 0 and tan(radians(9)) * x - y > 0:
            return loc + '8'
        
        if tan(radians(171)) * x - y > 0 and tan(radians(9)) * x - y < 0:
            return loc + '11'
        
        if tan(radians(153)) * x - y > 0 and tan(radians(171)) * x - y < 0:
            return loc + '14'
        
        if tan(radians(135)) * x - y > 0 and tan(radians(153)) * x - y < 0:
            return loc + '9'
        
        if tan(radians(117)) * x - y > 0 and tan(radians(135)) * x - y < 0:
            return loc + '12'
        
        if tan(radians(99)) * x - y > 0 and tan(radians(117)) * x - y < 0:
            return loc + '5'

    def generate_coordinates(self, aimpoint: tuple, r: int) -> tuple:

        xdist = randint(-r,r)
        ydist = randint(-r,r)
        x = aimpoint[0] + xdist
        y = aimpoint[1] + ydist
        return (x,y)




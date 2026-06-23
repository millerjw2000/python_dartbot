from random import *
from math import *
from sys import *

DIFFICULTY_COEFFICIENT = 1

aimpoints = {
    
    'T20':(0,111),
    'D20':(0,174),
    'S20':(0,142),
    
    'T19':(-34,-105),
    'D19':(-53,-165),
    'S19':(-43,-135),
    
    'T18':(65,89),
    'D18':(102,140),
    'S18':(83,114),
    
    'T17':(34,-105),
    'D17':(53,-165),
    'S17':(43,-135),
    
    'T16':(-89,-65),
    'D16':(-140,-102),
    'S16':(-114,-83),
    
    'T15':(89,-65),
    'D15':(140,-102),
    'S15':(114,-83),
    
    'T14':(-105,34),
    'D14':(-165,53),
    'S14':(-135,43),
    
    'T13':(105,34),
    'D13':(165,53),
    'S13':(135,43),
    
    'T12':(-65,89),
    'D12':(-102,140),
    'S12':(-83,114),
    
    'T11':(-111,0),
    'D11':(-174,0),
    'S11':(-142,0),
    
    'T10':(105,-34),
    'D10':(165,-53),
    'S10':(135,-43),
    
    'T9':(-89,65),
    'D9':(-140,102),
    'S9':(-114,83),
    
    'T8':(-105,-34),
    'D8':(-165,-53),
    'S8':(-135,-43),
    
    'T7':(-65,-89),
    'D7':(-102,-140),
    'S7':(-83,-114),
    
    'T6':(174,0),
    'D6':(142,0),
    'S6':(111,0),
    
    'T5':(-34,105),
    'D5':(-53,165),
    'S5':(-43,135),
    
    'T4':(89,65),
    'D4':(140,102),
    'S4':(114,83),
    
    'T3':(0,-111),
    'D3':(0,-174),
    'S3':(0,-142),
    
    'T2':(65,-89),
    'D2':(102,-140),
    'S2':(83,-114),
    
    'T1':(34,105),
    'D1':(53,165),
    'S1':(43,135),
    
    'BULL':(0,0),
    'DBULL':(0,0)
             
    }

def determine_hit(coordinates: tuple) -> str:
    
    x = int(coordinates[0])
    y = int(coordinates[1])

    loc = ''
    n = x**2 + y**2
    #print(x,y,n)
    
    if (n > 178**2):
        return 'MISS'
    elif (n > 170**2):
        loc += 'D'
    elif (170**2 > n > 115**2):
        loc += 'S'
    elif (115**2 > n > 107**2):
        loc += 'T'
    elif (107**2 > n > 16**2):
        loc += 'S'
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

def generate_coordinates(aimpoint: tuple, r: int) -> tuple:
    xdist = randint(-r,r)
    ydist = randint(-r,r)
    x = aimpoint[0] + xdist
    y = aimpoint[1] + ydist
    return (x,y)

def main():

    coords = generate_coordinates(aimpoints['T17'],30)
    print(determine_hit(coords))

if __name__ == '__main__':
    main()
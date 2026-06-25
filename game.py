import re
import copy

fresh_board = {     
                    
                    '20' : [0,20],
                    '19' : [0,19],
                    '18' : [0,18],
                    '17' : [0,17],
                    '16' : [0,16],
                    '15' : [0,15],
                    'BULL' : [0,25],
                    '0' : [0,0]
                }

acceptable_hits = [
                    '0',
                    '15',
                    'D15',
                    'T15',
                    '16',
                    'D16',
                    'T16',
                    '17',
                    'D17',
                    'T17',
                    '18',
                    'D18',
                    'T18',
                    '19',
                    'D19',
                    'T19',
                    '20',
                    'D20',
                    'T20',
                    'BULL',
                    'DBULL',
                ]

class Game:

    def __init__(self):
        
        self.player_scores = [0,0]
        self.player_boards = [
                            copy.deepcopy(fresh_board),
                            copy.deepcopy(fresh_board)
                            ]
        
    def check_for_win(self) -> bool:
        pass


    def update_scores(self) -> None:

        for player_index in range(2):

            player_score = 0

            for targ in self.player_boards[player_index].values():
                
                #print(targ)
                if targ[0] > 3:

                    n = targ[0] - 3
                    player_score += targ[1] * n

            self.player_scores[player_index] = player_score


    def enter_hit(self, player: int, hit: str) -> list:

        player_index = player - 1
   
        if hit.upper() not in acceptable_hits:

            
            #raise Exception(f"'{hit}' is not an acceptable entry")
            print(hit,'is not an acceptable entry - entering a 0')
            self.player_boards[player_index]['0'][0] += 1
            return self.player_boards
            


        if re.fullmatch(r"\d+", hit): # a single number

            self.player_boards[player_index][hit][0] += 1

        elif re.fullmatch(r"[A-Za-z]\d{1,2}", hit): # a double or triple + number

            if hit[0].upper() == 'T':
                    
                self.player_boards[player_index][hit[1:]][0] += 3

            elif hit[0].upper() == 'D':
                self.player_boards[player_index][hit[1:]][0] += 2

        elif hit.upper() == 'BULL': # bull

            self.player_boards[player_index][hit][0] += 1

        elif hit.upper() == 'DBULL': # double bull

            self.player_boards[player_index][hit][0] += 2

        self.update_scores()

        #print(self.player_scores[0],self.player_scores[1])
        return self.player_boards
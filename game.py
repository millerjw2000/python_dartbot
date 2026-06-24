import re
import copy

fresh_board = {     
                    '0' : [0,0],
                    '15' : [0,15],
                    '16' : [0,16],
                    '17' : [0,17],
                    '18' : [0,18],
                    '19' : [0,19],
                    '20' : [0,20],
                    'BULL' : [0,25]
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
                    '18',
                    'D19',
                    'T19',
                    '20',
                    'D20',
                    'T20',
                    'BULL',
                    'DBULL',
                ]

class Game:

    def __init__(self,difficulty):
        
        self.difficulty = difficulty

        self.player_scores = [0,0]
        self.player_boards = [
                            copy.deepcopy(fresh_board),
                            copy.deepcopy(fresh_board)
                            ]


    def update_scores(self) -> None:

        for player_index in range(2):

            player_score = 0

            for targ in self.player_boards[player_index].values():
                
                #print(targ)
                if targ[0] > 3:

                    n = targ[0] - 3
                    player_score += targ[1] * n

            self.player_scores[player_index] = player_score


    def enter_hits(self, player: int, entry: str) -> list:

        hits = entry.split()

        player_index = player - 1

        if 1 < player < 0:
            raise Exception('Invalid player selection')

        if len(hits) != 3:
            raise Exception('Invalid number of entries') 
        
        for hit in hits:
            
            if hit.upper() not in acceptable_hits:
                raise Exception(f"'{hit}' is not an acceptable entry")
            
        for hit in hits:

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

        print(self.player_scores[0],self.player_scores[1])
        return self.player_boards
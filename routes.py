from flask import Flask, render_template, request, redirect,jsonify
from flask_bootstrap import Bootstrap
import bot
import game

app = Flask(__name__)
bootstrap = Bootstrap(app)

global_game = None
global_bot = None

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/new_game')
def new_game():

    global global_game
    global_game = game.Game()

    global global_bot
    global_bot = bot.Bot(1)
    return render_template('game.html')

@app.route('/update_game',methods=["GET","POST"])
def update_game():

    if request.method == "POST":

        data = request.get_json()

        throws = data["throws"]
        print(throws)
        
        if len(throws) == 0:
            throws = ['0','0','0']
        elif len(throws) == 1:
            throws.append('0')
            throws.append('0')
        elif len(throws) == 2:
            throws.append('0')

        print(throws)
        # ['T20', '5', 'D20']
        response = {}
        response['winner'] = 0

        global_game.enter_hit(1,throws[0])
        global_game.enter_hit(1,throws[1])
        global_game.enter_hit(1,throws[2])

        if global_game.check_for_win() == True:

            response['winner'] = 1
        
        elif global_game.check_for_win() == False:

            response['bot_history'] = []
            
            for i in range(3):

                aimpoint = global_bot.decide_aimpoint(global_game)
                hit = global_bot.determine_hit(aimpoint)

                bot_move = f'Bot aimed at {aimpoint} and hit {hit}'
                print(bot_move)
                response['bot_history'].append(bot_move)

                global_game.enter_hit(2,hit)

            if global_game.check_for_win() == True:

                response['winner'] = 2
        
        response['player_1_board'] = global_game.player_boards[0]
        response['player_1_score'] = global_game.player_scores[0]
        response['player_2_board'] = global_game.player_boards[1]
        response['player_2_score'] = global_game.player_scores[1]

        return jsonify(response)
    
    if request.method == "GET":

        response = {}
        response['player_1_board'] = global_game.player_boards[0]
        response['player_1_score'] = global_game.player_scores[0]
        response['player_2_board'] = global_game.player_boards[1]
        response['player_2_score'] = global_game.player_scores[1]

        return jsonify(response)
        


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=16240)
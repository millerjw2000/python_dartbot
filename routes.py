from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import bot
import game
import jsonify

app = Flask(__name__)
bootstrap = Bootstrap(app)

global_game = ['']

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/new_game')
def new_game():

    current_game = game.Game()
    global_game[0] = current_game
    boards = current_game.player_boards
    scores = current_game.player_scores

    return render_template('game.html',boards=boards,scores=scores)

@app.route('/update_game',methods=["GET","POST"])
def update_game():

    if request.method == "POST":

        data = request.get_json()

        throws = data["throws"]

        print(throws)
        # ['T20', '5', 'D20']

        # update game

        return render_template("game.html",boards=global_game[0].player_boards,scores=global_game[0].player_scores)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=16240)
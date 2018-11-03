from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from controler import store_player_in_db, get_all_players, delete_player_from_db
app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/get-players', methods=['GET'])
def get_players():
    return jsonify(get_all_players())


@app.route('/store-player', methods=['POST'])
def store_player():
    store_player_in_db(request.get_json())
    return "I hope it went well"


@app.route('/delete-player/<int:id>', methods=['DELETE'])
def delete_player(id):
    delete_player_from_db(id)
    return "Deleting itme with id = {} ".format(id)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from flask_cors import CORS
from controler import store_player_in_db
app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/query-example')
def query_params():
    language = 'English'
    if 'language' in request.args.keys():
        language = request.args.get('language')
    return '''<h1>The chosen language is {}<h1>'''.format(language)


@app.route('/store-user', methods=['POST'])
def post_something():
    store_player_in_db(request.get_json())
    return "I hope it went well"


if __name__ == '__main__':
    app.run(debug=True)

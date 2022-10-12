import os
from flask import current_app, g
from json import JSONEncoder
from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello_vue')
def hello_vue():
    return render_template('hello_vue.html')

@app.route('/tlc_napkin')
def tlc_napkin():
    return render_template('tlc_napkin.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

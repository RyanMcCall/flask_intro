from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def roll_dice():
    return str(random.randint(1, 6))

@app.route('/roll-3-dice')
def roll_3_dice():
    return 'Roll 1:' + str(random.randint(1, 6)) + ' Roll 2:' + str(random.randint(1, 6)) + ' Roll 3:' + str(random.randint(1, 6))
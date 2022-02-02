from flask import Flask, render_template, request
from model import predict
import random

def roll_1d6():
    return random.randint(1, 6)

def roll_3d6():
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    roll_3 = random.randint(1, 6)
    return (roll_1, roll_2, roll_3)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Ryan')

@app.route('/roll-dice')
def roll_dice():
    return render_template('roll_dice.html', roll=roll_1d6())

@app.route('/roll-3-dice')
def roll_3_dice():
    return render_template('roll_3_dice.html', roll=roll_3d6())

@app.route('/my-first-form')
def my_first_form():
    return render_template('my_first_form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)

@app.route('/spam-detection')
def spam_detection():
    return render_template('spam_detection.html')

@app.route('/run-spam-detector', methods=['POST'])
def run_spam_detector():
    text_to_check = request.form['text_to_check']

    prediction = predict(text_to_check)

    return render_template('spam_detection_result.html', prediction=prediction)
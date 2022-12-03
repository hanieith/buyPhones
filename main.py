from flask import Flask, render_template, request
import telebot

bot = telebot.TeleBot('5806025745:AAEM-GLoUenhn8MPl9awRm0E7X1x-3o7GY4')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'


@app.route('/', methods=['GET', 'POST'])
def hello() -> str:
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        text = request.form['text']
        bot.send_message(-863962232, f'{name} {phone} {text}')
        print('succes')
    return render_template('index.html')


app.run()

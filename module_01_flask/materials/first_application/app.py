from flask import Flask


import datetime
import random


app:Flask = Flask(__name__)


cars_:str = 'Chevrolet, Renault, Ford, Lada'
cats_:list[str] = 'корниш-рекс, русская голубая, шотландская вислоухая, мейн-кун, манчкин.'.replace(',', '').replace('.', '').split()
count:int = 0


@app.route('/hello_world')
def hello_world():
    return 'привет мир и куратор который будет проверять дз :)'


@app.route('/cars')
def cars():
    return f'вот ваш список машин: {cars_}'


@app.route('/cats')
def cat():
    random_cat:str = random.choice(cats_)
    return f'какой ты кот на каждый день: {random_cat   }'

@app.route('/get_time')
def current_time_now():
    current_time:datetime = datetime.datetime.now()
    return f'времени сейчас {current_time}'


@app.route('/get_time/future')
def get_time_future():

    datetime_:list[str, str] = str(datetime.datetime.now()).split()
    date:list[str, str, str] = datetime_[0].split('-')
    time:list[str, str, str] = datetime_[1].split(':')

    if time[0].startswith('0') :
        time[0] = f'{time[0][1]}'
        time[0] = int(time[0]) + 1

        if time[0] == 24:
            time[0] = 0
            return f'дата: {date[0]} {date[1]} {int(date[2]) + 1}\nвремя: {time[0]} {time[1]} {time[2]}'

    return f'дата: {date[0]} {date[1]} {int(date[2]) }\nвремя: {time[0]} {time[1]} {time[2]}'


@app.route('/random_word')
def random_word():
    with open('war_and_peace.txt', 'r', encoding='utf-8') as file:
        text:list[str] = file.read().split()
        return f'{random.choice(text)}'


@app.route('/counter')
def counter():
    global count
    count += 1
    return f'страница открывалась {count} раз'
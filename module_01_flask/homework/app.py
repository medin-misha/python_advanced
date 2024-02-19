from flask import Flask
import random
import datetime
import os
app:Flask = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cars = ["Chevrolet", "Renault", "Ford", "Lada"]
cats = [ "корниш-рекс", "русская голубая", "шотландская вислоухая", 'мейн-кун', "манчкин"]
#hello world
@app.route('/hello_world')
def hello_world():
    return '|-_- |'

#cars
@app.route("/cars")
def cars_endpoint():
    global cars
    print(cars)
    return str(cars)

#cats
@app.route("/cats")
def random_cat_endpoint():
    global cats
    cat = cats[random.randint(0, len(cats) - 1)]
    return cat

#get_time now
@app.route("/get_time/now")
def get_time_now_endpoint():
    date_and_time = datetime.datetime.now()

    return f"точное дата и время: {date_and_time}"

#get_time future
@app.route("/get_time/future")
def get_future_time_endpoint():
    date_and_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"точное время через час: {date_and_time}"

#get_random_word
def get_text():
    with open(f"{BASE_DIR}\war_and_peace.txt", "r", encoding="UTF-8") as document:
        text = document.readlines()
    return text
text = get_text()


@app.route("/get_random_word")
def get_random_word_endpoint():
    global text
    result = text[random.randint(0, len(text) - 1)]
    return result
  
#counter
count = 0
@app.route("/counter")
def counter_endpoint():
    global count
    count += 1
    return f"{count}"
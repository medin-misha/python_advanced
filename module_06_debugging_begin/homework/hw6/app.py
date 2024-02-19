"""
Заменим сообщение "The requested URL was not found on the server" на что-то более информативное.
Например, выведем список всех доступных страниц с возможностью перехода по ним.

Создайте Flask Error Handler, который при отсутствии запрашиваемой страницы будет выводить
список всех доступных страниц на сайте с возможностью перехода на них.
"""

from flask import Flask

app = Flask(__name__)

all_adress:list =[
    "/dogs", '/cats',
    '/cats/1 or 2 or 2',
    "/index"
]
@app.route('/dogs')
def dogs():
    return 'Страница с пёсиками'


@app.route('/cats')
def cats():
    return 'Страница с котиками'


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'Страница с котиком {cat_id}'


@app.route('/index')
def index():

    return f'Главная страница'

@app.errorhandler(404)
def error_handler(error):
    return_str:str ="<h1>четыре</h1><h1>ноль</h1><h1>четыре</h1><h2>Введённый вами адресс не коректен или не существует попробуйте использовать:</h2> \n"
    for number, adress in enumerate(all_adress):
        return_str += f"<h3>{number + 1}) http://127.0.0.1:5000{adress}</h3>"

    return return_str, 404



if __name__ == '__main__':
    app.run(debug=True)

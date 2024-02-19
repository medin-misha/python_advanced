"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask

app = Flask(__name__)



"""
программа будет брать месяц и дату не как слово а как номер:
    не январь 12 число 2023 года
    а 01.12.2023
    потому что так всем проще и понятнее
"""

spending:dict = {}
date_dict: dict = {}
spending_per_year:int = 0
spending_per_year_mouth:int = 0



@app.route("/add/<date>/<int:number>")
def add(date: str, number: int, ):
    """
        сдесь идёт запись всех трат в виде
        {date}: {spending}
    """
    spending[date] = number

    for name, elem in spending.items():
        yield f'<p>{name}: {elem}</p>'

@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    """
    сдесь вводиться год и программа считает все траты в введённом году в виде :
    spending for {year}: {spending_per_year}
    """
    spending_per_year = 0
    for name, elem in spending.items():
        if name.endswith(f'{year}'):
            spending_per_year += int(elem)
    return f'<p>spending for {year}: {spending_per_year}</p>'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    """
    задание поставлено немного не коррекно я его понял вот так:
    сдесь вводиться год и месяц а вазвращяеться сумма всех трат в этом году в виде:
    <p>spending for {year}:{month}: {spending_per_year}</p>
    """
    spending_per_year = 0
    for name, elem in spending.items():
        if name.endswith(f'{year}') and name[:-5].endswith(f'{month}'):
            spending_per_year += int(elem)
    return f'<p>spending for {year}:{month}: {spending_per_year}</p>'

if __name__ == "__main__":
    app.run(debug=False)

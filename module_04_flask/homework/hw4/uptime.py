"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""
import ctypes
from flask import Flask

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    lib = ctypes.windll.kernel32


    time = lib.GetTickCount64()


    t = int(str(time)[:-3])


    mins, sec = divmod(time, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)


    return (f"{days} days, {hour:02}:{mins:02}:{sec:02}")


if __name__ == '__main__':
    app.run(debug=True)

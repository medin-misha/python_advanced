"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""
import json
import subprocess
import time
from typing import Any
import time
from functools import wraps

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

app = Flask(__name__)


def run_python_code_in_subproccess(
        code: str,
        )->str:
    code_return= subprocess.Popen(["python3", "-c",f'{code}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    code_return_result = code_return.stdout.read()
    return code_return_result.decode()

def controll_input_time(
        timeout:int)->Any:
    if 30 > timeout > 0:
        return None
    else:
        return ValueError


@app.route('/run_code',methods=['POST'] )
def run_code():

    data_form = request.get_data(as_text=True)
    data_object:dict = json.loads(data_form)
    try:
        code:str = data_object["code"]
        timeout:int = data_object["timeout"]
        controll_input_time(timeout=timeout)
        time = subprocess.Popen(["sleep", f"{timeout}"])
        result = run_python_code_in_subproccess(code=code)
        print(result)
        if time.poll() == None:
            return result
        else:
            return f"{time}"
    except ValueError:
        return "условие по которому вводиться время не соблюдено \n" \
               "время должно быть не больше 30 сек и не меньше 0 сек"
    except:
        return "ты ввёл что то не то"



if __name__ == '__main__':
    app.run(
        port = 5000,
        debug=True,
    )

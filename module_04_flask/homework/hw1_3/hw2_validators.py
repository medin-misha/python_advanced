"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
import json
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field, validators, StringField, IntegerField
from wtforms.validators import ValidationError, InputRequired

"""все глобальные переменные"""
messages:dict = {
                    "gmail":"Invalid email address.",
                     "name":"ты не ввёл имя",
                     "adress":"ты не ввёл адресс",
                     "index":"ты ввёл не коректный индекс",
                     "phoneNumber":"ты ошибся в номере телефона"
                }
def number_length(form: FlaskForm , field: Field):
    if len(field.data) != 9:
        raise ValidationError


class NumberLength:
    def __init__(self, number_count:int, message:str):
        self.number_count:int = number_count
        self.message:str = message
    def __call__(self, form: FlaskForm, field: Field):
        if len(field.data) != self.number_count:
            raise ValidationError(self.message)






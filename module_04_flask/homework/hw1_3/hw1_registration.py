"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from hw2_validators import number_length, NumberLength, messages
from wtforms.validators import InputRequired, NumberRange, Email

app = Flask(__name__)

class registrationForm(FlaskForm):

    gmail = StringField(validators=[InputRequired(message=messages["gmail"]), Email()])
    name = StringField(validators=[InputRequired(message=messages["name"])])
    adress = StringField(validators=[InputRequired(message=messages["adress"])])
    index = StringField(validators=[InputRequired(message=messages[ "index"]), NumberLength(number_count=5, message=messages["index"])])
    phoneNumber = StringField(validators=[InputRequired(message=messages["phoneNumber"]), NumberLength(number_count=9, message=messages["phoneNumber"])])
    comment = StringField()



@app.route("/register", methods = ["POST"])
def register_user():
    form = registrationForm()
    if form.validate_on_submit():
        User_email, phone  = form.gmail.data, form.phoneNumber.data
        return f"email - {User_email} phone - {phone}"
    return f"Error invalid Input {form.errors}"

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

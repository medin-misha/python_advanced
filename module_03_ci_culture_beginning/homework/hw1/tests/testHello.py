import unittest
from ..hello_word_with_day import app
import datetime

#TODO
class testWeekDay(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url:str = '/hello-world/'


    def testCanGetCorrectWeekDay(self):
        GREETINGS:tuple = (
            'Хорошего понедельника',
            'Хорошего вторника',
            'Хорошей среды',
            'Хорошего четверга',
            'Хорошей пятницы',
            'Хорошей субботы',
            'Хорошего воскресенья'
        )
        username:str = 'masa'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        numberWeekDay:int = datetime.datetime.today().weekday()

        self.assertTrue(GREETINGS[numberWeekDay] in response_text)


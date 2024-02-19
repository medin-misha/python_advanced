import unittest
#TODO
from ..app import app


class testApp(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url: str = '/add/'

    def testAdd(self):
        date:str = '12:12:1212/'
        money:int = 123
        response = self.app.get(f'{self.base_url}{date}{money}')
        response_text = response.data.decode()
        self.assertTrue('12:12:1212: 123' in response_text)
    def testCalculateYear(self):
        date: str = '12:12:1212/'
        money: int = 123
        response = self.app.get(f'{self.base_url}{date}{money}')
        responseInCalculate = self.app.get(f'/calculate/{date[6:10]}')
        response_text = responseInCalculate.data.decode()
        self.assertTrue('<p>spending for 1212: 123</p>' in response_text)
    def testCalculateYearMonth(self):
        date: str = '12:12:1212/'
        money: int = 123
        response = self.app.get(f'{self.base_url}{date}{money}')
        responseInCalculate = self.app.get(f'/calculate/{date[6:10]}/{date[3:5]}')
        response_text = responseInCalculate.data.decode()
        print(response_text)
        self.assertTrue('<p>spending for 1212:12: 123</p>' in response_text)


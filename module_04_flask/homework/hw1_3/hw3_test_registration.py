"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app
from hw2_validators import messages

class testValidators(unittest.TestCase):

    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/register'
        """вот сдесь нужно менять значения что бы выводилось всё коректно
        если ты хочешь вывести ошибку допустим gmail то меняй gmail"""

        self.form_data = {
            "gmail": "misha@gmail.com",
            "name": "Misha",
            "adress": "neznay",
            "index": 12645,
            "phoneNumber": 123456789,
        }

    def test_gmail_errors(self):
        response = self.app.post(self.base_url, data=self.form_data)
        response_text = response.data.decode()
        print(response_text)
        self.assertTrue(messages["gmail"] in response_text)
    def test_phone_number_errors(self):
        response = self.app.post(self.base_url, data=self.form_data)
        response_text = response.data.decode()
        print(response_text)
        self.assertTrue(messages["phoneNumber"] in response_text)

    def test_index_errors(self):
        response = self.app.post(self.base_url, data=self.form_data)
        response_text = response.data.decode()
        print(response_text)
        self.assertTrue(messages["index"] in response_text)



if __name__ == '__main__':
    unittest.main()

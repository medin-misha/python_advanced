import json
import unittest
from remote_execution import app

class test_my_program(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app_ = app.test_client()
        self.base_url = "/run_code"

    def test_my_app(self):
        post_reqest:str = '{"code":"import time; time.sleep(1);print(1)","timeout":2}'
        necessary_answer = b'1\n'
        response = self.app_.post(
            self.base_url,
            data = post_reqest
        ).data

        self.assertTrue(necessary_answer == response)

if __name__ == '__main__':
    unittest.main()

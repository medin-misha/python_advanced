import unittest
from block_errors import BlockErrors
class test_context_manager(unittest.TestCase):
    def test(self):
        errorList: list = [ValueError, TypeError]
        with BlockErrors(errorList):
            for i in range('123'):
                print(123)
        return True, "роботает нормально"
if __name__ == '__main__':
    unittest.main()

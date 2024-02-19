import unittest
from  ..person import Person
#TODO

class testForClassPerson(unittest.TestCase):
    def testGetAge(self):
        manMisha:Person = Person(name = 'Misha', year_of_birth=2008, address='china')
        function_res = manMisha.get_age()
        mishaAge:int = 15
        self.assertEqual(mishaAge, function_res)

    def testGetName(self):
        manMisha: Person = Person(name='Misha', year_of_birth=2008, address='china')
        function_res = manMisha.get_name()
        mishaName:str = 'Misha'
        self.assertEqual(mishaName, function_res)

    def testGetName(self):
        manMisha: Person = Person(name='Misha', year_of_birth=2008, address='china')
        function_res = manMisha.get_address()
        mishaAdress: str = 'china'
        self.assertEqual(mishaAdress, function_res)

    def testSetName(self):
        manMisha: Person = Person(name='Misha', year_of_birth=2008, address='china')
        function_res = manMisha.set_name('Uzbek')

        mishaNewName: str = 'имя изменено на Uzbek'
        self.assertEqual(mishaNewName, function_res)

    def testSetAdress(self):
        manMisha: Person = Person(name='Misha', year_of_birth=2008, address='china')
        function_res = manMisha.set_address('Uzbekistan')

        mishaNewAdress: str = 'адресс изменён на Uzbekistan'
        self.assertEqual(mishaNewAdress, function_res)

    def testIsHommlesNone(self):
        manMisha: Person = Person(name='Misha', year_of_birth=2008, address='')
        function_res = manMisha.is_homeless()
        mishaIsHome: bool = False
        self.assertEqual(mishaIsHome, function_res)

    def testIsHommlesNotNone(self):
        manMisha: Person = Person(name='Misha', year_of_birth=2008, address='Uzbekistan')
        function_res = manMisha.is_homeless()
        mishaIsHome: bool = True
        self.assertEqual(mishaIsHome, function_res)



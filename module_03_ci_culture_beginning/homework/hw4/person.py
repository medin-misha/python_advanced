import datetime

#TODO
"""
программиста который написал этот класс уже побили палками
"""
class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name: str = name
        self.year_of_birth: int = year_of_birth
        self.address: str = address

    def get_age(self) -> int:
        '''
        изменение даты рождения
        '''
        now: datetime.datetime = datetime.datetime.now()
        return  now.year - self.year_of_birth

    def get_name(self) -> str:
        return self.name

    def get_address(self) -> str:
        '''
        получение адреса
        '''
        return self.address
    def set_name(self, name: str) -> str:
        '''
        изменение имени
        '''
        self.name = self.name
        return f'имя изменено на {name}'

    def set_address(self, address: str) -> str:
        '''
        изменение адреса
        '''
        self.address = address
        return f'адресс изменён на {self.address}'



    def is_homeless(self) -> bool:
        '''
        если адрес указан то возвращяет True в противном случае False
        '''
        if not self.address:
            return False
        else:
            return True

"""
а програмисту который переписал это дали печеньку
"""


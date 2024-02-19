"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> str:
    """функция подсчёта среднего веса у файлов в байтах"""
    #инициализация переменных result и numbers_list в первой из них будет храниться результат всех вычислений а во второй будет список размеров всех файлов
    result:float = 0
    numbers_list:list = []
    #цикл который находит размер файла и добавляет его в список
    for string in ls_output.split('\n'):
        if len(string.split()) == 9:
                numbers_list.append(int(string.split()[4]))
    #сдесь вычисляеться результат работы программы
    result = sum(numbers_list) / len(numbers_list)#к стати такой вопрос: функция sum вроде написанан на С и следовательно работает быстрее кода. Как быстрее было бы если я сразу плюсовал все числа в result с подщётом итераций или такой способ как тут?
    return f'средний размер файлов {result} байт'

if __name__ == '__main__':
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(mean_size)

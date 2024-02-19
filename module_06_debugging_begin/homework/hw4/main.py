"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
from typing import Dict
import ast

def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as logsFile:
        message_list:dict = {
            'CRITICAL':0,
            'ERROR':0,
            'WARNING':0,
            'INFO':0,
            'DEBUG':0,
        }
        for i in logsFile:
            level:dict = dict(ast.literal_eval(i))["time"]
            match level:
                case "CRITICAL":
                    message_list["CRITICAL"] += 1
                case "ERROR":
                    message_list["ERROR"] += 1
                case "WARNING":
                    message_list["WARNING"] += 1
                case "INFO":
                    message_list["INFO"] += 1
                case "DEBUG":
                    message_list["DEBUG"] += 1
        return message_list






def task2() -> tuple:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as logsFile:
        time_list: dict = {

        }
        for i in logsFile:
            time: dict = dict(ast.literal_eval(i))["time"]
            if not f"t{time[0:2]}" in time_list:
                time_list[f"t{time[0:2]}"] = 1
            else:
                time_list[f"t{time[0:2]}"] += 1
            sorted_time_list:dict = sorted(time_list.items(), key=lambda x: x[1])
        return sorted_time_list[-1]


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as logsFile:
        time_critical_list: dict = {  }
        message_CRITICAL:int = 0
        for i in logsFile:
            message:dict = dict(ast.literal_eval(i))

            if int(message["time"].split(':')[0]) == 5 and \
                     0 < int(message["time"].split(':')[1]) < 20:
                message_CRITICAL += 1
                #print(f"{message['time']}:{message['level']}")
                message_CRITICAL += 1

            elif int(message["time"].split(':')[0]) == 5 and \
                    int(message["time"].split(':')[1]) == 21:
                break
    return message_CRITICAL

def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as logsFile:
        dog_count:int = 0
        for i in logsFile:
            message:dict = dict(ast.literal_eval(i))
            if "dog" in message["message"] :
                dog_count += 1
        return dog_count



def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    with open("skillbox_json_messages.log", "r", encoding="utf-8") as logsFile:
        vocabulary_words:dict = {  }
        for i in logsFile:
            messege:dict = dict(ast.literal_eval(i))["message"].split()
            for word in messege:
                if word in vocabulary_words:
                    vocabulary_words[word] += 1
                else:
                    vocabulary_words[word] = 0
    vocabulary_words_sorted = sorted(vocabulary_words.items(), key=lambda x: x[1])
    return vocabulary_words_sorted[-1]




if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')

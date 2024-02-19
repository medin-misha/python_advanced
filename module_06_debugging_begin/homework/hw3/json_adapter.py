"""
Удобно сохранять логи в определённом формате, чтобы затем их можно было фильтровать и анализировать. 
Сконфигурируйте логгер так, чтобы он писал логи в файл skillbox_json_messages.log в следующем формате:

{"time": "<время>", "level": "<уровень лога>", "message": "<сообщение>"}

Но есть проблема: если в message передать двойную кавычку, то лог перестанет быть валидной JSON-строкой:

{"time": "21:54:15", "level": "INFO", "message": "“"}

Чтобы этого избежать, потребуется LoggerAdapter. Это класс из модуля logging,
который позволяет модифицировать логи перед тем, как они выводятся.
У него есть единственный метод — process, который изменяет сообщение или именованные аргументы, переданные на вход.

class JsonAdapter(logging.LoggerAdapter):
  def process(self, msg, kwargs):
    # меняем msg
    return msg, kwargs

Использовать можно так:

logger = JsonAdapter(logging.getLogger(__name__))
logger.info('Сообщение')

Вам нужно дописать метод process так, чтобы в логах была всегда JSON-валидная строка.
"""

import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        data = {
            'time': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage()
        }
        return json.dumps(data)


if __name__ == '__main__':
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('skillbox_json_messages.json')
    file_handler.setFormatter(JsonFormatter())

    logger.addHandler(file_handler)

    message = 'This message contains a quote: "'
    logger.debug(message.replace('"', '\\"'))

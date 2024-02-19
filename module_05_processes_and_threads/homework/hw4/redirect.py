"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""
import sys
from types import TracebackType
from typing import Type, Literal, IO

import sys
import traceback
from types import TracebackType
from typing import Type, Literal, IO


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.__stdout__ = sys.stdout
        self.stdout = stdout
        self.__stderr__ = sys.stderr
        self.stderr = stderr

    def __enter__(self) -> None:
        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if self.stderr:
            sys.stderr.write(traceback.format_exc())

        sys.stdout = self.__stdout__
        sys.stderr = self.__stderr__

        if self.stderr:
            return True

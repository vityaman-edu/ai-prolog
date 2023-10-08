from enum import Enum
import logging
import os
from typing import AnyStr


class Log:
    class Level(Enum):
        Info = logging.INFO
        Debug = logging.DEBUG

    @classmethod
    def set_level(cls, level: Level):
        logging.basicConfig(level=level.value)

    @classmethod
    def debug(cls, message: AnyStr):
        '''
        https://stackoverflow.com/questions/10973362/python-logging-function-name-file-name-line-number-using-a-single-file
        '''
        import inspect
        function = inspect.currentframe().f_back.f_code
        name = function.co_name
        file = os.path.split(function.co_filename)[-1][:-3]
        line = function.co_firstlineno
        logging.debug(f'{file}:{name}:{line}: {message}')

    @classmethod
    def info(cls, message: str):
        import inspect
        function = inspect.currentframe().f_back.f_code
        name = function.co_name
        file = os.path.split(function.co_filename)[-1][:-3]
        line = function.co_firstlineno
        logging.info(f'{file}:{name}:{line}: {message}')

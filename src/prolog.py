from typing import List
from log import Log as log
from pyswip import Prolog as SWIProlog
from pyswip.core import cleanupProlog


class Prolog:
    def __init__(self, preload: List[str]):
        self.__pl: SWIProlog = None
        self.__preload = preload

    def query(self, query: str):
        log.debug(query)
        return self.__pl.query(query)

    def is_proven(self, query: str) -> bool:
        log.debug(query)
        return bool(list(self.query(query)))

    def assume(self, fact: str):
        log.debug(fact)
        self.__pl.assertz(fact)

    def __enter__(self):
        self.__pl = SWIProlog()
        for file in self.__preload:
            self.__pl.consult(file)
        return self

    def __exit__(self, *args, **kvargs):
        # FIXME: segfault on duoble call inside a one process
        cleanupProlog()

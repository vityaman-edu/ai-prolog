import os
from typing import NamedTuple, List
import sys


class Args(NamedTuple):
    knowledge_path: str

    @property
    def preload(self) -> List[str]:
        path = self.knowledge_path
        return [f'res/{file}' for file in os.listdir(path)]

    @classmethod
    def parse(cls, args: List[str]) -> 'Args':
        return Args(
            knowledge_path=args[1],
        )

    @classmethod
    def system(cls) -> 'Args':
        return cls.parse(sys.argv)

import os
from typing import NamedTuple, List
import sys


class Args(NamedTuple):
    knowledge_path: str
    echo: bool = False

    @property
    def preload(self) -> List[str]:
        path = self.knowledge_path
        return [f'res/{file}' for file in os.listdir(path) if file.endswith('.pl')]

    @classmethod
    def parse(cls, args: List[str]) -> 'Args':
        return Args(
            knowledge_path=args[1],
            echo=True if len(args) > 2 and args[2] == 'echo' else False
        )

    @classmethod
    def system(cls) -> 'Args':
        return cls.parse(sys.argv)

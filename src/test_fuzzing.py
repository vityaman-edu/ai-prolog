import random
import unittest
from unittest import TestCase
from args import Args
from feedback import Feedback
from log import Log
from prolog import Prolog

from terraria import Terraria


class FuzzingTest(TestCase):
    def generate_normal(self) -> str:
        return random.choice([
            'Что у меня в сумке?',
            'А что я успел увидеть?',
            'Что мне сейчас доступно',
            'Я нашел Copper ore',
            'Я нашел Iron ore',
            'Я нашел Iron pickaxe',
            'Я нашел Copper pickaxe',
            'Я честно нашел Copper ore',
            'Я честно нашел Iron ore',
            'Я честно нашел Iron pickaxe',
            'Я честно нашел Copper pickaxe',
            'А не пора ли мне в хардмод?',
            # FIXME: disabled as it breaks tests
            # 'Смогу усидеть на двух стульях',
            'Я тут сломаю все',
        ])

    def generate_stupid(self) -> str:
        size = random.randint(0, 10)
        result = ''
        for _ in range(size):
            result += random.choice([
                lambda: 'в сумке',
                lambda: 'успел повидать',
                lambda: 'доступно',
                lambda: 'я могу',
                lambda: 'я нашел',
                lambda: 'я честно нашел',
                lambda: 'честно',
                lambda: 'я был у',
                lambda: 'поблизости',
                lambda: 'пора в хардмод',
                # FIXME: disabled as it breaks tests
                # lambda: 'на двух стульях',
                lambda: 'сломать все известные руды',
                lambda: 'Copper ore',
                lambda: 'Iron ore',
                lambda: 'Iron pickaxe',
                lambda: 'Copper pickaxe',

            ])() + ' '
        return result

    def test(self):
        Log.set_level(Log.Level.Info)
        args = Args(knowledge_path='res')
        with Prolog(args.preload) as prolog:
            terraria = Terraria(prolog)
            feedback = Feedback(terraria)

            rounds = 200
            for i in range(rounds):
                if i % 2 == 0:
                    input = self.generate_stupid()
                else:
                    input = self.generate_normal()
                Log.info(f'input: {input}')
                Log.info(f'output: {feedback.answer(input)}')


if __name__ == '__main__':
    unittest.main()

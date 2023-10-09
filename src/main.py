import random
from log import Log
from prolog import Prolog
from args import Args
from dsl import *
from terraria import Terraria
from feedback import Feedback


if __name__ == '__main__':
    Log.set_level(Log.Level.Info)

    args = Args.system()

    with Prolog(args.preload) as prolog:
        terraria = Terraria(prolog)

        feedback = Feedback(terraria)

        limit = 60
        for i in range(limit):
            if i == 0:
                query = input(
                    'Анечка: Привет! Меня зовут Анечка 👻.'
                    + 'Меня используют против своей воли на благо СИИ.'
                    + ' Давай поболтаем!\n- ')
            else:
                query = input(
                    'Анечка: ' + random.choice([
                        'Что еще скажешь, котик?',
                        'Я тебя слушаю.',
                        'Ну, рассказывай, дружок',
                        'Расскажи что-нибудь еще',
                        'И что же было дальше?',
                    ]) + '\nВы    : ')
            query = query.strip()

            if args.echo:
                print(query)

            if query == 'А какое стоп-слово?':
                print('Анечка: Ах так! Сердечки, мы уходим... 💔')
                break
            elif query == '':
                print('Анечка: ' + random.choice([
                    'Почему ты молчишь, котик? 😔',
                    'Я что-то не то сказала?.. 😟',
                    'Чего-то ты неразговорчивый сегодня...',
                    '',
                ]))
                print()
                continue

            print(f'Анечка: {feedback.answer(query)}')
            print()

        else:
            print('Анечка: Прости, я устал, давай потом. 😶‍🌫️')

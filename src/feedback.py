
from typing import Callable
import random
import re

from terraria import Terraria, TerrariaException


def emotion(): return random.choice([
    'Ничего себе',
    'Ого',
    'Вау',
    'А ты хорош',
    'ПУПУПУМ',
    'ППААААМ',
])


def on_show_inventory(terraria: Terraria, groups) -> str:
    inventory = terraria.inventory()
    if len(inventory) == 0:
        return random.choice([
            'Ой, кажется, у тебя ничего нееет 😊',
            'Ничего не вижу. Кто-то на мели...🤭',
            'Пусто! Но ты не волнуйся, когда-то и я был бедным студентом 🤓',
        ])
    else:
        return f'{emotion()}! У тебя целых {len(inventory)} предметов! 🫢\n'\
            + ',\n'.join(map(lambda w: '-> ' + w, map(repr, inventory)))


def on_show_places(terraria: Terraria, groups):
    places = terraria.places()
    if len(places) == 0:
        return random.choice([
            'Тебе бы хоть разочек выйти из дома что ли... 🫤',
            'Ты серьезно ходил(а) ТОЛЬКО в универ все это время?! 😳',
            'Ты еще ничего не видел(а) в этой жизни...'
        ])
    return f'{emotion()}! Ты видел уже {len(places)} вещей! 🫢\n'\
        + ',\n'.join(map(lambda w: '-> ' + w, map(repr, places)))


def on_show_available(terraria: Terraria, groups):
    available = terraria.available()
    if len(available) == 0:
        return random.choice([
            'У тебя нет будущего... 🥲',
            'Состояние безысходности... 🫤',
            'Не знаешь, что делать дальше? Я тоже. 😐',
        ])
    return f'Не знаешь, что делать дальше? Попробуй добыть что-нибудь из этого списка!\n'\
        + ',\n'.join(map(lambda w: '-> ' + w, map(repr, available)))


def on_action_take(terraria: Terraria, groups):
    name = groups[-2][0] + groups[-2][1:].lower()
    type = groups[-1].lower()
    try:
        if type not in ('ore', 'pickaxe'):
            return 'Стоп! Можно брать только ore или pickaxe!'
        terraria.take(f'{type}(\'{name}\')')
        return random.choice([
            f'{emotion()}! Рад за тебя, милаш! 😚',
            f'Ах, ты ж моя молодчинка',
            f'{emotion()}! Крутышка!',
        ])
    except TerrariaException as e:
        return random.choice([
            f'Оййй 🤕. Ну ты чего? Как же можно взять недоступное?',
            f'Возьми нормально 😡',
            f'Просто так даже {name} {type} не возьмется! ⚒️',
            f'В сказку попал(a)? 🙃'
        ])


def on_action_cheat(terraria: Terraria, groups):
    name = groups[-2][0] + groups[-2][1:].lower()
    type = groups[-1].lower()
    if type not in ('ore', 'pickaxe'):
        return f'Стоп! Можно брать только ore или pickaxe, но никак не {type}!'
    terraria.cheat(f"{type}('{name}')")
    return random.choice([
        'Обманываешь меня... Ну, ладно, первый и последний раз. 😤',
        'Ладно, но только потому что мы друзья. Мы же друзья?.. 🥶',
        'Чего только не сделаешь ради друга. Ладно! 🤫'
    ])


def on_action_explore(terraria: Terraria, groups):
    name = groups[-2][0] + groups[-2][1:].lower()
    type = groups[-1].lower()
    if type not in ('evil_biome', 'ore'):
        return f'Ну evil_biome и ore еще куда не шло, но {type}... Ты чего, зайчик?'
    terraria.explore(f'{type}(\'{name}\')')
    return random.choice([
        f'Нашел {name} {type}? Теперь попробуй найти себе тяночку. 😆',
        'А вы путешествинник. Молодой Афанасий-Никитин?',
        f'{emotion()}! Ну и находка!',
    ])


def on_check_is_ready_for_hardmode(terraria: Terraria, groups):
    if terraria.is_ready_for_hardmode():
        return random.choice([
            f'{emotion()}! Молодец, теперь ты можешь отправиться во второй модуль!',
            'Да, почему бы и нет, валяй, чибрик!',
        ])
    return random.choice([
        'Не торопись, сначала тебе нужна адская кирка.',
        'К сожалению, ты пока не готов(а)',
        'Да какой тебе хардмод, милаш?',
        'Не торопи жизнь',
    ])


def on_check_is_able_to_craft_both_evil_pickaxe(terraria: Terraria, groups):
    if terraria.is_able_to_craft_both_evil_pickaxe():
        return random.choice([
            'Как вы этого добились?',
            f'{emotion()}! Можешь!'
        ])
    return random.choice([
        'Кажется, что нет.',
        'Не-а',
        '😔',
    ])


def on_check_is_able_to_break_all_explored_ores(terraria: Terraria, groups):
    if terraria.is_able_to_break_all_explored_ores():
        return random.choice([
            'Да, ты можешь',
            'Угу',
        ])
    return random.choice([
        'Бро, нужно тренироваться',
        'Нужно больше кирок королю кирок',
    ])


def on_error(terraria: Terraria, groups):
    return random.choice([
        'Со мной нужно поговорить через чат. Чат я дала. Чтобы знать, что спрашивать, нужен гайд. Гайд я не дам.',
        'Ничего не понял, но очень интересно! 😁',
        'Прости... я тебя не понимаю...😔',
        'Не пон, попробуй перефразировать, пожалуйста 🧐'
    ])


class Feedback:
    def __init__(self, terraria: Terraria):
        self.terraria = terraria
        self.patterns = {
            r'.*в.*сумке.*': on_show_inventory,
            r'.*успел.*(повидать|увидеть).*': on_show_places,
            r'.*(доступно|я могу|способен).*': on_show_available,
            r'.*(ну+)?.*я( же )? .*(честно|правда).*наше+л (\w+) (\w+).*': on_action_cheat,
            r'.*(нашел|собрал|сделал|взял|добыл) (\w+) (\w+).*': on_action_take,
            r'.*я .*был (прямо? )?((у)|(рядом с)|(поблизости к)) ([a-zA-z_]+) ([a-zA-z_]+).*': on_action_explore,
            r'.*пора.* в хардмод.*': on_check_is_ready_for_hardmode,
            r'.*на двух стульях.*': on_check_is_able_to_craft_both_evil_pickaxe,
            r'.*слом(ать|аю).* все известные руды.*': on_check_is_able_to_break_all_explored_ores,
        }
        self.fallback = on_error

    def answer(self, input: str) -> str:
        for pattern in self.patterns:
            match = re.match(pattern, input, re.IGNORECASE)
            if match is None:
                continue
            try:
                return self.patterns[pattern](
                    self.terraria, match.groups())
            except Exception as e:
                print('Error', e)
                return 'Я умираю, прости... Прощай, друг! 🤧'
        else:
            return self.fallback(self.terraria, None)

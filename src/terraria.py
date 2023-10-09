from typing import Any, Generator, List, Set
from prolog import Prolog
from dsl import *
from parse import Expr
from itertools import chain


class TerrariaException(Exception):
    pass


class Terraria:
    def __init__(self, state: Prolog):
        self._state = state

    def cheat(self, item: Item):
        self._state.assume(found(item))

    def is_available(self, item: Item) -> bool:
        return self._state.is_proven(available(item))

    def take(self, item: Item):
        if not self.is_available(item):
            raise TerrariaException(
                'can not take an item as it is not available')
        self.cheat(item)

    def explore(self, object: NatureObject):
        self._state.assume(found(existing(object)))

    def all_items(self) -> Set[Expr]:
        def generate():
            for type in ('ore', 'pickaxe'):
                for item in self._state.query(f'{type}(A)'):
                    item = Expr.parse(item['A'])
                    item = Expr(type, item)
                    yield item
        return set(generate())

    def inventory(self) -> Set[Expr]:
        def generate():
            for item in self._state.query(found('Item')):
                item = Expr.parse(item['Item'])
                if item.is_existing:
                    continue
                yield item
        return set(generate())

    def available(self) -> Set[Expr]:
        def generate():
            inventory = set(self.inventory())
            for item in self.all_items():
                if self.is_available(item) and item not in inventory:
                    yield item
        return set(generate())

    def places(self) -> Set[Expr]:
        def generate():
            for item in self._state.query(found('Item')):
                item = Expr.parse(item['Item'])
                if item.is_existing:
                    yield item
        return set(generate())

    def is_ready_for_hardmode(self) -> bool:
        statement = "achived('Can break all found existing ores')"
        return self._state.is_proven(statement)

    def is_able_to_craft_both_evil_pickaxe(self) -> bool:
        statement = "achived('Theoretically can craft both Nightmare and Deathbringer')"
        return self._state.is_proven(statement)

    def is_able_to_break_all_explored_ores(self) -> bool:
        statement = "achived('Is ready to hardmode')"
        return self._state.is_proven(statement)

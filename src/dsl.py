from enum import Enum

from parse import Expr


EvilBiome = Enum('EvilBiome', [
    'Crimson',
    'Corruption',
])
EvilBiome.__str__ = lambda self: f"evil_biome('{self.name}')"
EvilBiome.__repr__ = lambda self: f"{repr(Expr.parse(str(self)))}"

Ore = Enum('Ore', [
    'Copper',
    'Tin',
    'Iron',
    'Lead',
    'Silver',
    'Tungsten',
    'Gold',
    'Platinum',
    'Meteorite',
    'Demonite',
    'Crimtane',
    'Obsidian',
    'Hellstone',
    'Cobalt',
    'Palladium',
    'Mythril',
    'Orichalcum',
    'Adamantite',
    'Titanium',
    'Chlorophyte',
    'Luminite',
])
Ore.__str__ = lambda self: f"ore('{self.name}')"
Ore.__repr__ = lambda self: f"{repr(Expr.parse(str(self)))}"


Pickaxe = Enum('Pickaxe', [
    'Cactus',
    'Copper',
    'Tin',
    'Iron',
    'Lead',
    'Silver',
    'Tungsten',
    'Gold',
    'Platinum',
    'Nightmare',
    'Deathbringer',
    'Molten',
    'Cobalt',
    'Palladium',
    'Mythril',
    'Orichalcum',
    'Adamantite',
    'Titanium',
])
Pickaxe.__str__ = lambda self: f"pickaxe('{self.name}')"
Pickaxe.__repr__ = lambda self: f"{repr(Expr.parse(str(self)))}"

Item = Pickaxe | Ore


NatureObject = EvilBiome | Ore

def existing(thing: object) -> str:
    return f'existing({thing})'


def found(thing: object) -> str:
    return f'found({thing})'


def available(item: Item) -> str:
    return f'available({item})'

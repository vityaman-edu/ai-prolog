:- module(requirement, [requirement/2]).

:- use_module(pickaxe).
:- use_module(ore).
:- use_module(evil).

requirement(pickaxe('Copper'), ore('Copper')).
requirement(pickaxe('Tin'), ore('Tin')).
requirement(pickaxe('Iron'), ore('Iron')).
requirement(pickaxe('Lead'), ore('Lead')).
requirement(pickaxe('Silver'), ore('Silver')).
requirement(pickaxe('Tungsten'), ore('Tungsten')).
requirement(pickaxe('Gold'), ore('Gold')).
requirement(pickaxe('Platinum'), ore('Platinum')).
requirement(pickaxe('Nightmare'), ore('Demonite')).
requirement(pickaxe('Deathbringer'), ore('Crimtane')).
requirement(pickaxe('Molten'), ore('Hellstone')).
requirement(pickaxe('Cobalt'), ore('Cobalt')).
requirement(pickaxe('Palladium'), ore('Palladium')).
requirement(pickaxe('Mythril'), ore('Mythril')).
requirement(pickaxe('Orichalcum'), ore('Orichalcum')).
requirement(pickaxe('Adamantite'), ore('Adamantite')).
requirement(pickaxe('Titanium'), ore('Titanium')).

requirement(ore(Ore), pickaxe_with_power(PickaxePower)) :-
    ore_power(ore(Ore), PickaxePower).

requirement(ore('Demonite'), evil_biome('Corruption')).
requirement(ore('Crimtane'), evil_biome('Crimson')).

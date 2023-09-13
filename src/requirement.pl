:- module(requirement, [requirement/2]).

:- use_module(pickaxe, [pickaxe_power/2]).
:- use_module(ore, [ore_power/2]).

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

requirement(ore(Ore), pickaxe(Pickaxe)) :- 
    ore_power(ore(Ore), OrePower),
    pickaxe_power(pickaxe(Pickaxe), PickaxePower),
    (PickaxePower < OrePower -> false ; true).

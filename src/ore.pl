:- module(ore, [ore/1, ore_power/2, existing/1]).

ore('Copper').
ore('Tin').
ore('Iron').
ore('Lead').
ore('Silver').
ore('Tungsten').
ore('Gold').
ore('Platinum').
ore('Meteorite').
ore('Demonite').
ore('Crimtane').
ore('Obsidian').
ore('Hellstone').
ore('Cobalt').
ore('Palladium').
ore('Mythril').
ore('Orichalcum').
ore('Adamantite').
ore('Titanium').
ore('Chlorophyte').
ore('Luminite').

existing(ore(Ore)) :- ore(Ore).

ore_power(ore('Copper'), 1).
ore_power(ore('Tin'), 1).
ore_power(ore('Iron'), 2).
ore_power(ore('Lead'), 2).
ore_power(ore('Silver'), 3).
ore_power(ore('Tungsten'), 3).
ore_power(ore('Gold'), 4).
ore_power(ore('Platinum'), 4).
ore_power(ore('Meteorite'), 4).
ore_power(ore('Demonite'), 5).
ore_power(ore('Crimtane'), 5).
ore_power(ore('Obsidian'), 5).
ore_power(ore('Hellstone'), 6).
ore_power(ore('Cobalt'), 7).
ore_power(ore('Palladium'), 7).
ore_power(ore('Mythril'), 8).
ore_power(ore('Orichalcum'), 9).
ore_power(ore('Adamantite'), 10).
ore_power(ore('Titanium'), 11).

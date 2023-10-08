:- module(pickaxe, [
    pickaxe/1, 
    pickaxe_power/2,
    pickaxe_with_power/1
]).

pickaxe('Cactus').
pickaxe('Copper').
pickaxe('Tin').
pickaxe('Iron').
pickaxe('Lead').
pickaxe('Silver').
pickaxe('Tungsten').
pickaxe('Gold').
pickaxe('Platinum').
pickaxe('Nightmare').
pickaxe('Deathbringer').
pickaxe('Molten').
pickaxe('Cobalt').
pickaxe('Palladium').
pickaxe('Mythril').
pickaxe('Orichalcum').
pickaxe('Adamantite').
pickaxe('Titanium').

pickaxe_power(pickaxe('Cactus'), 2).
pickaxe_power(pickaxe('Copper'), 2).
pickaxe_power(pickaxe('Tin'), 2).
pickaxe_power(pickaxe('Iron'), 3).
pickaxe_power(pickaxe('Lead'), 3).
pickaxe_power(pickaxe('Silver'), 4).
pickaxe_power(pickaxe('Tungsten'), 4).
pickaxe_power(pickaxe('Gold'), 5).
pickaxe_power(pickaxe('Platinum'), 5).
pickaxe_power(pickaxe('Nightmare'), 6).
pickaxe_power(pickaxe('Deathbringer'), 6).
pickaxe_power(pickaxe('Molten'), 7).
pickaxe_power(pickaxe('Cobalt'), 8).
pickaxe_power(pickaxe('Palladium'), 8).
pickaxe_power(pickaxe('Mythril'), 9).
pickaxe_power(pickaxe('Orichalcum'), 9).
pickaxe_power(pickaxe('Adamantite'), 10).
pickaxe_power(pickaxe('Titanium'), 10).

pickaxe_with_power(1).
pickaxe_with_power(2).
pickaxe_with_power(3).
pickaxe_with_power(4).
pickaxe_with_power(5).
pickaxe_with_power(6).
pickaxe_with_power(7).
pickaxe_with_power(8).

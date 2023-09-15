:- module(progress, [found/1]).

:- use_module(pickaxe).

found(evil_biome('Crimson')).

found(ore('Copper')).
found(pickaxe('Copper')).
found(pickaxe('Gold')).

found(pickaxe_with_power(Power)) :-
    found(pickaxe(Pickaxe)),
    pickaxe_power(pickaxe(Pickaxe), PickaxePower),
    (PickaxePower < Power -> false ; true).

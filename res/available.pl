:- module(available, [available/1]).

:- use_module(progress).
:- use_module(requirement).

available(Item) :- 
    Item, found(Item).

available(ore(Ore)) :-
    found(existing(ore(Ore))),
    ore_power(ore(Ore), OrePower),
    findall(Pickaxe, (
        pickaxe(Pickaxe),
        pickaxe_power(pickaxe(Pickaxe), PickaxePower),
        (PickaxePower < OrePower -> false; true),
        found(pickaxe(Pickaxe))
    ), Pickaxes),
    member(_, Pickaxes).

available(Item) :- 
    Item,
    findall(R, requirement(Item, R), Requirements),
    member(_, Requirements),
    forall(member(R, Requirements), found(R)).

:- module(reachable, [reachable/1]).

:- use_module(requirement).
:- use_module(available).

:- use_module(pickaxe).

reachable(Item) :- 
    Item, available(Item).

reachable(pickaxe_with_power(TargetPower)) :-
    findall(Pickaxe, (
        pickaxe(Pickaxe),
        pickaxe_power(pickaxe(Pickaxe), PickaxePower),
        (PickaxePower < TargetPower -> false; true)
    ), Pickaxes),
    member(FirstPickaxe, Pickaxes),
    reachable(pickaxe(FirstPickaxe)).

reachable(Item) :- 
    Item,
    findall(R, requirement(Item, R), Requirements),
    member(_, Requirements),
    forall(member(R, Requirements), reachable(R)).


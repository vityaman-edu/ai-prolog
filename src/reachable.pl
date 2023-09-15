:- module(reachable, [reachable/1]).

:- use_module(requirement).
:- use_module(available).

reachable(Item) :- 
    Item, available(Item).
reachable(Item) :- 
    Item,
    findall(R, requirement(Item, R), Requirements),
    member(_, Requirements),
    forall(member(R, Requirements), reachable(R)).

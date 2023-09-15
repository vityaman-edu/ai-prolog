:- module(available, [available/1]).

:- use_module(progress).
:- use_module(requirement).

available(Item) :- 
    Item, found(Item).
available(Item) :- 
    Item,
    findall(R, requirement(Item, R), Requirements),
    member(_, Requirements),
    forall(member(R, Requirements), found(R)).

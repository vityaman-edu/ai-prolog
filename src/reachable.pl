:- module(reachable, [reachable/1]).

:- use_module(requirement).
:- use_module(available).

reachable(Item) :- 
    Item, available(Item).
reachable(Item) :- 
    Item, requirement(Item, Requirement), reachable(Requirement).

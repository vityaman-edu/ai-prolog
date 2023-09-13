:- module(available, [available/1]).

:- use_module(progress).
:- use_module(requirement).

available(Item) :- 
    Item, found(Item).
available(Item) :- 
    Item, requirement(Item, Requirement), found(Requirement).

:- module(achievements, [achived/1]).

:- use_module(ore).
:- use_module(pickaxe).
:- use_module(available).
:- use_module(reachable).

achived('Can break all found existing ores') :-
    forall(
        found(existing(ore(Ore))), 
        available(ore(Ore))
    ).

achived('Theoretically can craft both Nightmare and Deathbringer') :-
    reachable(pickaxe('Nightmare')), 
    reachable(pickaxe('Deathbringer')).

achived('Is ready to hardmode') :- 
    available(pickaxe('Molten')).

:- use_module(ore).
:- use_module(pickaxe).
:- use_module(requirement).
:- use_module(reachable).
:- use_module(available).
:- use_module(progress).
:- use_module(evil).

print_fact(Fact) :-
    Fact, write('+ '), writeln(Fact).
print_fact(Fact) :-
    \+ Fact, write('- '), writeln(Fact).

?- nl.
?- writeln('Progress:').
?- print_fact(found(evil_biome('Corruption'))).
?- print_fact(found(evil_biome('Crimson'))).
?- print_fact(found(ore('Copper'))).
?- print_fact(found(pickaxe('Copper'))).
?- print_fact(found(ore('Iron'))).
?- print_fact(found(pickaxe('Iron'))).
?- print_fact(found(ore('Gold'))).
?- print_fact(found(pickaxe('Gold'))).
?- print_fact(found(ore('Demonite'))).
?- print_fact(found(pickaxe('Nightmare'))).
?- nl.
?- writeln('Availablility: ').
?- print_fact(available(ore('Copper'))).
?- print_fact(available(pickaxe('Copper'))).
?- print_fact(available(ore('Iron'))).
?- print_fact(available(pickaxe('Iron'))).
?- print_fact(available(ore('Silver'))).
?- print_fact(available(pickaxe('Silver'))).
?- print_fact(available(ore('Gold'))).
?- print_fact(available(pickaxe('Gold'))).
?- print_fact(available(ore('Demonite'))).
?- print_fact(available(pickaxe('Nightmare'))).
?- print_fact(available(ore('Crimtane'))).
?- print_fact(available(pickaxe('Deathbringer'))).
?- nl.
?- writeln('Reachability: ').
?- print_fact(reachable(ore('Copper'))).
?- print_fact(reachable(pickaxe('Copper'))).
?- print_fact(reachable(ore('Iron'))).
?- print_fact(reachable(pickaxe('Iron'))).
?- print_fact(reachable(ore('Silver'))).
?- print_fact(reachable(pickaxe('Silver'))).
?- print_fact(reachable(ore('Gold'))).
?- print_fact(reachable(pickaxe('Gold'))).
?- print_fact(reachable(ore('Demonite'))).
?- print_fact(reachable(pickaxe('Nightmare'))).
?- print_fact(reachable(ore('Crimtane'))).
?- print_fact(reachable(pickaxe('Deathbringer'))).
?- nl.

:- use_module(ore).
:- use_module(pickaxe).
:- use_module(requirement).
:- use_module(reachable).
:- use_module(available).
:- use_module(progress).

print_fact(Fact) :-
    Fact, write('+ '), writeln(Fact).
print_fact(Fact) :-
    \+ Fact, write('- '), writeln(Fact).

?- nl.
?- writeln('Progress:').
?- print_fact(found(ore('Copper'))).
?- print_fact(found(pickaxe('Copper'))).
?- print_fact(found(ore('Iron'))).
?- print_fact(found(pickaxe('Iron'))).
?- nl.

?- writeln('Availablility: ').
?- print_fact(available(ore('Copper'))).
?- print_fact(available(pickaxe('Copper'))).
?- print_fact(available(ore('Iron'))).
?- print_fact(available(pickaxe('Iron'))).
?- print_fact(available(ore('Silver'))).
?- print_fact(available(pickaxe('Silver'))).
?- nl.

?- writeln('Reachability: ').
?- print_fact(reachable(ore('Copper'))).
?- print_fact(reachable(pickaxe('Copper'))).
?- print_fact(reachable(ore('Iron'))).
?- print_fact(reachable(pickaxe('Iron'))).
?- print_fact(reachable(ore('Silver'))).
?- print_fact(reachable(pickaxe('Silver'))).
?- nl.

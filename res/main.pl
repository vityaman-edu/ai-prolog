:- use_module(ore).
:- use_module(pickaxe).
:- use_module(requirement).
:- use_module(reachable).
:- use_module(available).
:- use_module(progress).
:- use_module(evil).
:- use_module(achievements).

print_fact(Fact) :-
    Fact, write('+ '), writeln(Fact).
print_fact(Fact) :-
    \+ Fact, write('- '), writeln(Fact).

% ?- nl.
% ?- writeln('Progress:').
% ?- print_fact(found(evil_biome('Corruption'))).
% ?- print_fact(found(evil_biome('Crimson'))).
% ?- print_fact(found(ore('Copper'))).
% ?- print_fact(found(pickaxe('Copper'))).
% ?- print_fact(found(ore('Iron'))).
% ?- print_fact(found(pickaxe('Iron'))).
% ?- print_fact(found(ore('Gold'))).
% ?- print_fact(found(pickaxe('Gold'))).
% ?- print_fact(found(ore('Demonite'))).
% ?- print_fact(found(pickaxe('Nightmare'))).
% ?- print_fact(found(ore('Hellstone'))).
% ?- print_fact(found(pickaxe('Molten'))).
% ?- nl.
% ?- writeln('Availablility: ').
% ?- print_fact(available(ore('Copper'))).
% ?- print_fact(available(pickaxe('Copper'))).
% ?- print_fact(available(ore('Iron'))).
% ?- print_fact(available(pickaxe('Iron'))).
% ?- print_fact(available(ore('Silver'))).
% ?- print_fact(available(pickaxe('Silver'))).
% ?- print_fact(available(ore('Gold'))).
% ?- print_fact(available(pickaxe('Gold'))).
% ?- print_fact(available(ore('Demonite'))).
% ?- print_fact(available(pickaxe('Nightmare'))).
% ?- print_fact(available(ore('Crimtane'))).
% ?- print_fact(available(pickaxe('Deathbringer'))).
% ?- print_fact(available(ore('Hellstone'))).
% ?- print_fact(available(pickaxe('Molten'))).
% ?- nl.
% ?- writeln('Reachability: ').
% ?- print_fact(reachable(ore('Copper'))).
% ?- print_fact(reachable(pickaxe('Copper'))).
% ?- print_fact(reachable(ore('Iron'))).
% ?- print_fact(reachable(pickaxe('Iron'))).
% ?- print_fact(reachable(ore('Silver'))).
% ?- print_fact(reachable(pickaxe('Silver'))).
% ?- print_fact(reachable(ore('Gold'))).
% ?- print_fact(reachable(pickaxe('Gold'))).
% ?- print_fact(reachable(ore('Demonite'))).
% ?- print_fact(reachable(pickaxe('Nightmare'))).
% ?- print_fact(reachable(ore('Crimtane'))).
% ?- print_fact(reachable(pickaxe('Deathbringer'))).
% ?- print_fact(reachable(ore('Hellstone'))).
% ?- print_fact(reachable(pickaxe('Molten'))).
% ?- nl.
% ?- writeln('Achivements: ').
% ?- print_fact(achived('Can break all found existing ores')).
% ?- print_fact(achived('Theoretically can craft both Nightmare and Deathbringer')).
% ?- print_fact(achived('Is ready to hardmode')).
% ?- nl.

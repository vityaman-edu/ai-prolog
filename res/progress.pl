:- module(progress, [found/1]).

:- use_module(pickaxe).
:- use_module(ore).

:- dynamic(found/1).

% found(evil_biome('Crimson')).
% 
% found(existing(ore('Crimtane'))) :- 
%     found(evil_biome('Crimson')).
% found(existing(ore('Demonite'))) :- 
%     found(evil_biome('Corruption')).
% 
% found(existing(ore('Demonite'))).
% 
% found(existing(ore('Tin'))).
% found(existing(ore('Iron'))).
% found(existing(ore('Silver'))).
% found(existing(ore('Gold'))).
% 
% found(existing(ore('Hellstone'))).
% 
% found(ore('Copper')).
% found(pickaxe('Copper')).
% found(pickaxe('Gold')).
% found(pickaxe('Deathbringer')).
% found(pickaxe('Molten')).
% 

found(pickaxe_with_power(Power)) :-
    number(Power),
    found(pickaxe(Pickaxe)),
    pickaxe_power(pickaxe(Pickaxe), PickaxePower),
    (PickaxePower < Power -> false ; true).

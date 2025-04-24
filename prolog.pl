% Facts
male(john).
male(michael).
male(david).
male(james).

female(susan).
female(linda).
female(emily).
female(sarah).

parent(john, michael).
parent(john, linda).
parent(susan, michael).
parent(susan, linda).
parent(michael, david).
parent(emily, david).
parent(linda, sarah).
parent(james, sarah).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

siblings(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    X \= Y.

grandparent(X, Y) :- 
    parent(X, Z), 
    parent(Z, Y).

grandfather(X, Y) :- 
    male(X), 
    grandparent(X, Y).

grandmother(X, Y) :- 
    female(X), 
    grandparent(X, Y).

uncle(X, Y) :- 
    male(X), 
    siblings(X, Z), 
    parent(Z, Y).

aunt(X, Y) :- 
    female(X), 
    siblings(X, Z), 
    parent(Z, Y).

cousins(X, Y) :- 
    parent(Z, X), 
    siblings(Z, W), 
    parent(W, Y).
##use https://swish.swi-prolog.org/p/VNixUnyg.pl to run
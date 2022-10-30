"""Algorithme Exercice 2 Partie A 3) a)"""


def carre(n):
    s = 0

    for i in range(n + 1):
        s += i**2
    return s

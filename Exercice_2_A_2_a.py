"""Algorithme Exercice 2 Partie A 2) a)"""


def sommeP(n):
    if n == 0:
        return n

    s = 0

    for i in range(n + 1):
        s += 2 * i
    return s

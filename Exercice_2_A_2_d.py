"""Algorithme Exercice 2 Partie A 2) d)"""


def sommeP2(n):
    if n == 0:
        return n

    s = 0
    i = 0

    while 2 * i < n:
        s += 2 * i
        i += 1
    return s

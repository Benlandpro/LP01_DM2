"""Algorithme Exercice 2 Partie B c)"""


def fact(n):
    p = n

    for i in range(1, n):
        p *= n - i
    return p


nb = int(input("Saisir l'entier N: "))
print("N! =", fact(nb))

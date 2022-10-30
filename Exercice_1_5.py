"""Algorithme Exercice 1 5)"""
prixCafe = float(input("Prix Café sélectionné: "))
mntPaye = float(input("Montant payé: "))

if mntPaye > prixCafe:
    monnaie = mntPaye - prixCafe
    print("Monnaie rendue " + str(monnaie))
else:
    aPayer = prixCafe - mntPaye
    print("Restant a payer: " + str(aPayer))


import numpy as np

# 1. Demander le nombre d'etats
n = int(input("Entrez le nombre d'etats : "))

# 2. Creer une matrice Q remplie de zeros
Q = np.zeros((n, n))

# 3. Saisir les taux de transition entre les etats differents
print("Entrez les taux de transition q(i,j) pour i != j :")
for i in range(n):
    for j in range(n):
        if i != j:
            Q[i][j] = float(
                input(f"Entrez q[{i+1}][{j+1}] : ")
            )

# 4. Calculer les coefficients diagonaux
# q(i,i) = - somme des q(i,j), pour j different de i

for i in range(n):
    Q[i][i] = -np.sum(Q[i])

# Afficher le generateur Q
print("\nGenerateur infinitesimal Q :")
print(Q)

# 5. Verifier les taux de transition
valide = True

for i in range(n):
    for j in range(n):
        if i != j and Q[i][j] < 0:
            valide = False

if not valide:
    print("Erreur : les taux de transition doivent etre positifs ou nuls.")

else:
    print("\nQ est un generateur infinitesimal valide.")

    # 6. Construire le systeme Pi * Q = 0
    A = Q.T.copy()

    # Ajouter la condition somme(Pi) = 1
    A[-1] = np.ones(n)

    # Creer le second membre
    b = np.zeros(n)
    b[-1] = 1

    # 7. Resoudre le systeme
    try:
        Pi = np.linalg.solve(A, b)
        
        # 8. Afficher la distribution stationnaire
        print("\nDistribution stationnaire :")

        for i in range(n):
            print(f"π{i+1} = {Pi[i]:.4f}")

        print("\nVérification de la somme de πi:")
        print(f"Somme = {np.sum(Pi):.4f}")

    except np.linalg.LinAlgError:
        print("Le systeme ne peut pas etre resolu directement.")
        print("La distribution stationnaire peut ne pas etre unique.")

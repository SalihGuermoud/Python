nbPierreMax = int(input())
hauteur = 0
nbPierreNecessaire = 0

while nbPierreMax > nbPierreNecessaire:
    hauteur = hauteur + 1
    nbPierreNecessaire = nbPierreNecessaire + ((hauteur)*(hauteur))
    
print(hauteur)
print(nbPierreNecessaire)


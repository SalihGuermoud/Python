# Calcul et affichage du prix ttc

saisie = input("Votre valeur : ")
prixHorsTaxe = int (saisie)
tauxTva = 0.05
coefTva = 1 + tauxTva

prixTtc = (prixHorsTaxe) * coefTva



print(prixTtc)

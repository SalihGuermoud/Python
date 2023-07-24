def ligne(n, car):
    """Affiche une ligne de , caractères"""
    for loop in range(n):
        print(car, end = "")
        
def bordure(car):
    print(car, end = "")
    
def motif(largeur, car):
    """Affiche une ligne d'espace encadrés
       Ne passe pas à la ligne !
       largeur doit >= 3"""
    
    bordure(car)
    ligne(largeur - 2, " ")
    bordure(car)
    
    
def carre(n):
    """
       Affiche un carré de côté n (caractères) n >= 1
    """
    CAR = "#"
    ligne(n, CAR)
    print()
    if n == 1:
        nbMotifs = 0
    else:
        nbMotifs = n - 2
    for loop in range(nbMotifs):
        motif(n, CAR)
    if n != 1:
        ligne(n, CAR)
        
def triangle(n):
    """ Affiche le triangle de hauteur n"""
    CAR = "@"
    ligne(1, CAR)
    if n > 1:
        ligne(2, CAR)
        for loop in range(n-3):
            motif(loop + 3, CAR)
            print()
        ligne(n, CAR)
        print()
#le programme débute ici
taille = int(input())
ligne(taille, "X")
print()
carre(taille)
print()
triangle(taille)

""" Test motif()
for i in range(3, 5):
    motif(i, "M")
"""    
def ligneRectangle():
    print("#", end = "")
    

def afficherFigures():
    afficherLigneX()
    afficherRectangle()
    afficherTriangle()

def afficherLigneX():
    for i in range(nbX):
        print("X", end = "")
    print()
nbX = int(input())


def afficherRectangle():
    ligneRectangle()
    for j in range(nbLignesRectangle):
        
        
    for k in range(nbColonnesRectangle):
        print("#", end = "" )
    print()
nbLignesRectangle = int(input())
nbColonnesRectangle = int(input())    

    
def afficherTriangle():
    for l in range(nbLignesTriangle):
        print("@")
nbLignesTriangle = int(input())

afficherFigures()
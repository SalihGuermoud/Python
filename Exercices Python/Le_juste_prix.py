"https://www.france-ioi.org/algo/task.php?idChapter=647&idTask=1944"

nbMarchands = int(input())
prixBas = 1000000
resultat = 0
position = 0

for loop in range(nbMarchands):
    prixGalettes = int(input())
    position = position + 1
    
    if(prixGalettes < prixBas or prixGalettes == prixBas):
        prixBas = prixGalettes
        resultat = position
        
    
print(resultat)

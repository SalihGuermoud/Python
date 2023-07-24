"https://www.france-ioi.org/algo/task.php?idChapter=648&idTask=1974"

dateDebut = int(input())
dateFin = int(input())
nbEntrees = int(input())
resultat = 0

for loop in range(nbEntrees):
    dateEntree = int(input())
    
    if(dateEntree >= dateDebut and dateEntree <= dateFin):
        resultat = resultat + 1
print(resultat)        
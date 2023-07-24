"""https://www.france-ioi.org/algo/task.php?idChapter=647&idTask=1945"""

pa = int(input())
nbVillage = int(input())
resultat = 0

for loop in range(nbVillage):
    pv = int(input())
    villageProcheAvant = pv <= pa and pv >= pa - 50
    villageProcheApres = pv >= pa and pv <= pa + 50
    
    if (villageProcheAvant or villageProcheApres):
        resultat = resultat + 1
print(resultat)    
    